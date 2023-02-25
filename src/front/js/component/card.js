import React from "react";

export default function Card() {
  return (
    <div>
      <div className="card">
        <img src={cpic} className="card-img-top" />
        <div className="card-body">
          <h5 className="card-title">{cTitle + " - " + cPrice}</h5>
          <button href={cLink} className="btn btn-primary">
            Buy Now
          </button>
        </div>
      </div>
    </div>
  );
}
