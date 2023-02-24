import React from "react";
import Button from "@material-ui/core/Button";
import Popover from "@material-ui/core/Popover";
import { Link } from "react-router-dom";

export default function PopoverDemo() {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);

  return (
    <div className="container">
      <button title="List View" className="listBtn">
        <Link to={"/scholars_study/list"}>
          <div className="fa-solid fa-border-all fa-2xl"></div>
        </Link>
      </button>
      <h2 className="roomHeader">The Scholar's Study</h2>
      <div className="roomBtnContainer">
        <img className="roomImg" src="https://i.imgur.com/jG5GOPdh.png" />
          <div style={{ display: "block", padding: 30 }} className="roomBtnContainer">
            <Button
              className="studyBtn"
              onClick={(event) => {
                setAnchorEl(event.currentTarget);
              }}
            >
              <div className="fa-regular fa-circle-dot fa-2xl studyOne"></div>
            </Button>
            <Popover
              anchorEl={anchorEl}
              open={open}
              id={open ? "simple-popover" : undefined}
              onClose={() => {
                setAnchorEl(null);
              }}
              transformOrigin={{
                horizontal: "center",
                vertical: "top",
              }}
              anchorOrigin={{
                horizontal: "center",
                vertical: "bottom",
              }}
            >
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
            </Popover>
          </div>
      </div>
    </div>
  );
}
