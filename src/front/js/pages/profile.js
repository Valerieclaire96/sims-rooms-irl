import React,  { useContext } from "react";
import { Context } from "../store/appContext";
import SimsCard from "../component/simsCard";

export default function Profile() {
  const { store, actions } = useContext(Context);
    let favorites = store.favorites
    
  return(
  <div className="container">
    <div style={{ width: "100%", postion: "inline-block" }}>
      <img
        src="http://dw52ywakuajj6.cloudfront.net/memories/SimMemories1920x1080.jpg"
        style={{ height: "300px", width: "100%" }}
      ></img>
      <img
        className="profilePic"
        src="https://gameranx.com/wp-content/uploads/2022/05/Sims-4-Smiling-Sim-1024x576.jpg"
        style={{
          height: "200px",
          width: "200px",
          right: "43.5%",
          objectFit: "cover",
          top: "30%",
          position: "absolute",
        }}
      ></img>
    </div>
    <h2 style={{
          right: "30%",
          top: "45%",
          position: "absolute",
        }}>{`${store.user_name}`}</h2>
        <h3 style={{ marginTop:"100px"}}>Favorites</h3>
        
        <div className='profileCardGrid'>
                { favorites.length > 0 &&
                    favorites.map((item, idx) => {
                        console.log(item);
                        return (
                            <div  key={idx}>
                                <SimsCard  id={item.id} />
                            </div>                            
                        )}
                    )  
                }
    </div>
  </div>
 )
} 
