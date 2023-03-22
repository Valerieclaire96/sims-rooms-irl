import React from "react";
import "../../styles/roomSelector.css";
import { Link } from "react-router-dom";

export default function roomImages() {
  return (
    <div className="container text-center">
    <div className="catContainer row row-cols-auto">
      <div className="room col">
        <Link to="/room/1">
        <img
        className="catImg"
          src="https://i.imgur.com/SmhGAwI.png"
          alt="Dude, Where's my Closet?"
        />
        </Link>
        <h4>Dude, Where's my Closet?</h4>
      </div>
      <div className="room col">
        <Link to="/room/2">
        <img
          className="catImg"
          src="https://i.imgur.com/MT1HV5j.png"
          alt="geeks4sleep"
        />
        </Link>
        <h4>sleep4geeks</h4>
      </div>
      <div className="room col">
        <Link to="/room/3">
        <img
          className="catImg"
          src="https://i.imgur.com/9WdnFoR.png"
          alt="Lazy Susan's Kitchen"
        />
        </Link>
        <h4>Lazy Susan's Kitchen</h4>
      </div>
      <div className="room col">
        <Link to="/room/4">
        <img
          className="catImg"
          src="https://i.imgur.com/tPG1Meg.png"
          alt="Quick Bites, Long Talks"
        />
        </Link>
        <h4>Quick Bites, Long Talks</h4>
      </div>
      <div className="room col">
        <Link to="/room/5">
        <img
          className="catImg"
          src="https://i.imgur.com/jG5GOPd.png"
          alt="The Fancy Man's Study"
        />
        </Link>
        <h4>The Fancy Man's Study</h4>
      </div>
      <div className="room col">
        <Link to="/room/6">
        <img
          className="catImg"
          src="https://i.imgur.com/YpAijUT.png"
          alt="Straight As to Zzz"
        />
        </Link>
        <h4>Straight As to Zzz</h4>
      </div>
      
      <div className="room col">
        <Link to="/room/7">
        <img
          className="catImg"
          src="https://i.imgur.com/HHILH8C.png"
          alt="Tweenage Dirtbag"
        />
        </Link>
        <h4>Tweenage Dirtbag</h4>
      </div>
      <div className="room col">
        <Link to="/room/8">
        <img
          className="catImg"
          src="https://i.imgur.com/iaJefXz.png"
          alt="Unicorn Dreams"
        />
        </Link>
        <h4>Unicorn Dreams</h4>
      </div>
      <div className="room col">
        <Link to="/room/9">
        <img
          className="catImg"
          src="https://i.imgur.com/2W36O5V.png"
          alt="Vroom Room"
        />
        </Link>
        <h4>Vroom Room</h4>
      </div>
      <div className="room col">
        <Link to="/room/10">
        <img
          className="catImg"
          src="https://i.imgur.com/6aHMhet.png"
          alt="Zen Den"
        />
        </Link>
        <h4>Zen Den</h4>
      </div>
    </div>
    </div>
  );
}
