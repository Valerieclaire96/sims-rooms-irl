import React, { useState, useEffect, useContext} from "react";
import { Context } from "../store/appContext";


const defaultRealObjectInfo = {id:null, sims_names:'this object', real_pic_url: "https://m.media-amazon.com/images/I/413hQe6UPQL._AC_.jpg", buy_url: "https://a.co/d/8WBBavf", price:16}
export default function RealCard({id}) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [ objectList, setObjectList] = useState(defaultRealObjectInfo);


  useEffect(() => {
    async function fetchData() {
    const res = await fetch(
      process.env.BACKEND_URL + "/api/objects/" + id
    )
      const data = await res.json()
      console.log("//room objects by id", data)
        setObjectList(data);
  }; fetchData();
  }, [id]);

  return (
    <div>
      <div className="card">
        <img src={objectList.real_pic_url} className="card-img-top" />
        <div className="card-body">
          <h5 className="card-title">{objectList.sims_names + " - $" + objectList.price}</h5>
          <button href={objectList.buy_url} className="btn btn-primary">
            Buy Now
          </button>
        </div>
      </div>
    </div>
  );
}
