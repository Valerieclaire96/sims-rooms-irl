import React, { useState } from "react";
import { Link } from "react-router-dom";
import Popover from "@material-ui/core/Popover";
import Button from "@material-ui/core/Button";

export default function ScholarsStudy({cPic,cTitle, cPrice, cLink}) {
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
        <Button
          className="studyBtn studyOne"
          onClick={(event) => {
            setAnchorEl(event.currentTarget);
          }}
        >
          <div className="fa-regular fa-circle-dot fa-2xl"></div>
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
        <Button
          className="studyBtn studyTwo boxOverlay"
          onClick={(event) => {
            setAnchorEl(event.currentTarget);
          }}
        >
          <div className="fa-regular fa-circle-dot fa-2xl"></div>
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
      
      <Button
          className="studyBtn studyThree boxOverlay"
          onClick={(event) => {
            setAnchorEl(event.currentTarget);
          }}
        >
          <div className="fa-regular fa-circle-dot fa-2xl"></div>
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
        <Button
          className="studyBtn studyFour boxOverlay"
          onClick={(event) => {
            setAnchorEl(event.currentTarget);
          }}
        >
          <div className="fa-regular fa-circle-dot fa-2xl"></div>
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
        <Button
          className="studyBtn studyFive boxOverlay"
          onClick={(event) => {
            setAnchorEl(event.currentTarget);
          }}
        >
          <div className="fa-regular fa-circle-dot fa-2xl"></div>
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
        <Button
          className="studyBtn studySix boxOverlay"
          onClick={(event) => {
            setAnchorEl(event.currentTarget);
          }}
        >
          <div className="fa-regular fa-circle-dot fa-2xl"></div>
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
          <h3>Featured</h3>
          <div className="cardContainerMain">
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
                src="https://i.imgur.com/i0yK226.png"
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
                src="https://i.imgur.com/N1qG0Fm.png"
                className="card-img-top"
                alt="..."
              />
              <div className="card-body">
                <h5 className="card-title">Card title</h5>
                <a href="#" className="btn btn-primary">
                  Go somewhere
                </a>
              </div>
            </div>
            <div className="card">
              <img
                src="https://i.imgur.com/p4leMsk.png"
                className="card-img-top"
                alt="..."
              />
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
