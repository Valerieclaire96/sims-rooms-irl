import React from "react";
import { Link } from "react-router-dom";

export default function ScholarsList() {
  return (
    <div className="container selection">
      <button title="Room View" className="listBtn">
        <Link to={"/scholars_study"}>
          <div className="fa-solid fa-border-all fa-2xl"></div>
        </Link>
      </button>
      <h2 className="roomHeader">The Scholar's Study</h2>
      <div className="roomCardContainer">
        <div className="cardContainer">
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
        </div>
        {/* 2 */}
        <div className="cardContainer">
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
        </div>
        {/* 3 */}
        <div className="cardContainer">
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
        </div>
        {/* 4 */}
        <div className="cardContainer">
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
        </div>
        {/* 5 */}
        <div className="cardContainer">
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
        </div>
        {/* 6 */}
        <div className="cardContainer">
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
          <div className="card">
            <img
              src="https://i.imgur.com/HBs0rHW.png"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <h5 className="card-title">Card title</h5>
              <button href="#" className="btn btn-primary">
                Go somewhere
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
