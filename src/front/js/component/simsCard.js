import { CardActions } from "@material-ui/core";
import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";

const defaultRealObjectInfo = {
  id: null,
  sims_names: "this object",
  real_pic_url: "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7d4d7c61-796e-421e-80f6-d565fd221647/d7nb9s6-d1a837cf-c615-44ed-9f8a-2224547dba6a.png/v1/fill/w_900,h_507,q_80,strp/sims_4_cas_inspired_wallpaper___plumbob_by_moozdeviant_d7nb9s6-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTA3IiwicGF0aCI6IlwvZlwvN2Q0ZDdjNjEtNzk2ZS00MjFlLTgwZjYtZDU2NWZkMjIxNjQ3XC9kN25iOXM2LWQxYTgzN2NmLWM2MTUtNDRlZC05ZjhhLTIyMjQ1NDdkYmE2YS5wbmciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0._jTWxHrCUgz7uz1Szr1-rgC26aBP8CL67dB57B3halM",
  buy_url: "https://a.co/d/8WBBavf",
  price: 16,
};
export default function SimsCard({ id }, props) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [objectList, setObjectList] = useState(defaultRealObjectInfo);
  const {store, actions} = useContext(Context)
  let objectInfo = {"name" : objectList.sims_names, "buy" :objectList.buy_url, "pic":objectList.sims_pic_url, "price":objectList.price}
  // console.log("object list HERE", objectInfo)

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(process.env.BACKEND_URL + "/api/objects/" + id);
      const data = await res.json();
      console.log("//room objects by id", data);
      setObjectList(data);
    }
    fetchData();
  }, [id]);


  const handleClick = (e) => {
    e.preventDefault();
    actions.addFavorite(objectInfo)
  }

  return (
    <div>
      <div className="card" style={{width:"18rem"}}>
        <img src={objectList.sims_pic_url} className="card-img-top" />
        <div className="card-body">
          <h5 style={{height:"60px"}} className="card-title mt-2">
            {objectList.sims_names + " - $" + objectList.price}
          </h5>
          <div className="cardBottom">
            <a href={objectList.buy_url} target="blank">
              <button className="btn btn-info mb-2">Buy Now</button>
            </a>
            <button onClick={(e) => handleClick(e)} className="fa-sharp fa-regular fa-heart" style={{background: "transparent", border: "none", outline:"none",}}></button>
          </div>
        </div>
      </div>
    </div>
  );
}
