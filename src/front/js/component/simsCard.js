import React, { useState, useEffect } from "react";


const defaultSimsObjectInfo = {id:null, name:"thisObject", sims_names:"thisCard", sims_pic_url:"https://i.imgur.com/ZDVzExF.png", buy_url: "https://a.co/d/8WBBavf", price:16}
export default function SimsCard({id}) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [ objectInfo, setObjectInfo] = useState(defaultSimsObjectInfo);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(
        process.env.BACKEND_URL + "/api/objects/" + id  
      )
      const data = await res.json()
  
        setObjectInfo(data);
  }; fetchData();
  }, [id]);

  return (
    <div>
      <div className="card">
        <img src={objectInfo.sims_pic_url} className="card-img-top" />
        <div className="card-body">
          <h5 className="card-title">{objectInfo.sims_names + " - $" + objectInfo.price}</h5>
          <button href={objectInfo.buy_url} className="btn btn-primary">
            Buy Now
          </button>
        </div>
      </div>
    </div>
  );
}
