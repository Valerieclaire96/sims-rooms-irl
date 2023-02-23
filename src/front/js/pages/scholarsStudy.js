import React from "react";
import { Link } from "react-router-dom";

export default function ScholarsStudy() {
  return (
    <div className="container">
      <button title="List View" className="listBtn"><Link to={"/scholars_study/list"}><div className="fa-solid fa-border-all fa-2xl"></div></Link></button>
      <h2 className="roomHeader">The Scholar's Study</h2>
      <div className="roomBtnContainer">
        <img className="roomImg"src="https://i.imgur.com/jG5GOPdh.png"/>
          <span className="roomBtn"><button className="studyBtn"><div className="fa-regular fa-circle-dot studyOne fa-2xl"></div></button></span>
          <span className="roomBtn"><button className="studyBtn"><div className="fa-regular fa-circle-dot studyTwo fa-2xl"></div></button></span>
          <span className="roomBtn"><button className="studyBtn"><div className="fa-regular fa-circle-dot studyThree fa-2xl"></div></button></span>
          <span className="roomBtn"><button className="studyBtn"><div className="fa-regular fa-circle-dot studyFour fa-2xl"></div></button></span>
          <span className="roomBtn"><button className="studyBtn"><div className="fa-regular fa-circle-dot studyFive fa-2xl"></div></button></span>
          <span className="roomBtn"><button className="studyBtn"><div className="fa-regular fa-circle-dot studySix fa-2xl"></div></button></span>
      </div>
      <h3>Featured</h3>
      <div className="cardContainerMain">
      <div className="card">
        <img src="https://i.imgur.com/HBs0rHW.png" className="card-img-top" alt="..." />
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <button href="#" className="btn btn-primary">
            Go somewhere
          </button>
        </div>
      </div>
      <div className="card">
        <img src="https://i.imgur.com/i0yK226.png" className="card-img-top" alt="..." />
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <button href="#" className="btn btn-primary">
            Go somewhere
          </button>
        </div>
      </div>
      <div className="card">
        <img src="https://i.imgur.com/N1qG0Fm.png" className="card-img-top" alt="..." />
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <a href="#" className="btn btn-primary">
            Go somewhere
          </a>
        </div>
      </div>
      <div className="card">
        <img src="https://i.imgur.com/p4leMsk.png" className="card-img-top" alt="..." />
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <a href="#" className="btn btn-primary">
            Go somewhere
          </a>
        </div>
      </div>
    </div>
    </div>
  );
}
