import React from "react";
import { Link } from "react-router-dom";

export default function ScholarsStudy() {
  return (
    <div className="roomContainer">
      <button className="roomBtn"><Link to={"/scholars_study/list"}></Link><i class="fa-solid fa-grip-vertical"></i></button>
      <div>
        <img className="room image"src="https://i.imgur.com/jG5GOPdh.png"/>
          <span className="roomBtn"></span>
          <span className="roomBtn"></span>
          <span className="roomBtn"></span>
          <span className="roomBtn"></span>
          <span className="roomBtn"></span>
          <span className="roomBtn"></span>
          <span className="roomBtn"></span>
          <span className="roomBtn"></span>
          <span className="roomBtn"></span>
      </div>
    </div>
  );
}
