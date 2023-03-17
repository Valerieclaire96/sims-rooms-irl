import React from "react";
import SimsCard from "../component/simsCard";

export default function Profile() {
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
          right: "42.55%",
          top: "30%",
          position: "absolute",
        }}
      ></img>
    </div>
    <h2 style={{
          right: "30%",
          top: "45%",
          position: "absolute",
        }}>Shelly Sims</h2>
      <img className="favRoom" src="https://i.imgur.com/6aHMhet.png" style={{ height: "500px", width: "70%", marginTop:"100px"}}></img>
      <h3>Favorite Rooms</h3>
    <div className="d-flex mt-3 mb-3 favObjects">
      {/* ask on how to make this better */}
      <SimsCard id={Math.floor(Math.random() * 68 + 1)} />
      <SimsCard id={Math.floor(Math.random() * 68 + 1)} />
      <SimsCard id={Math.floor(Math.random() * 68 + 1)} />
    </div>
    <h3>Favorite Objects</h3>
  </div>
 )
} 
