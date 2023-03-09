import React, { useState, useEffect } from "react";


const defaultRealObjectInfo = {id:null, sims_names:'this object', real_pic_url: "https://m.media-amazon.com/images/I/413hQe6UPQL._AC_.jpg", buy_url: "https://a.co/d/8WBBavf", price:16}
export default function RealCard({id}) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [ realObjectInfo, setRealObjectInfo] = useState(defaultRealObjectInfo);

  useEffect(async() => {
    const res = await fetch(
      "https://3001-valerieclai-simsroomsir-xyu3edngwba.ws-us89b.gitpod.io/api/objects/" + id
    )
      const data = await res.json()

        setRealObjectInfo(data);
  }, [id]);

  return (
    <div>
      <div className="card">
        <img src={realObjectInfo.real_pic_url} className="card-img-top" />
        <div className="card-body">
          <h5 className="card-title">{realObjectInfo.sims_names + " - $" + realObjectInfo.price}</h5>
          <button href={realObjectInfo.buy_url} className="btn btn-primary">
            Buy Now
          </button>
        </div>
      </div>
    </div>
  );
}
