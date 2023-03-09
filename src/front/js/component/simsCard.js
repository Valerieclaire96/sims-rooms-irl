import React, { useState, useEffect } from "react";


const defaultSimsObjectInfo = {id:null, name:"thisObject", sims_names:"thisCard", sims_pic_url:"https://i.imgur.com/ZDVzExF.png", buy_url: "https://a.co/d/8WBBavf", price:16}
export default function SimsCard({id}) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [ simsObjectInfo, setSimsObjectInfo] = useState(defaultSimsObjectInfo);

  useEffect(async() => {
    const res = await fetch(
      "https://3001-valerieclai-simsroomsir-xyu3edngwba.ws-us89b.gitpod.io/api/objects/" + id
    )
      const data = await res.json()

        setSimsObjectInfo(data);
  }, [id]);

  return (
    <div>
      <div className="card">
        <img src={simsObjectInfo.sims_pic_url} className="card-img-top" />
        <div className="card-body">
          <h5 className="card-title">{simsObjectInfo.sims_names + " - $" + simsObjectInfo.price}</h5>
          <button href={simsObjectInfo.buy_url} className="btn btn-primary">
            Buy Now
          </button>
        </div>
      </div>
    </div>
  );
}
