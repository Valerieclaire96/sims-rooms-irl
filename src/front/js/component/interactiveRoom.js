import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Popover from "@material-ui/core/Popover";
import Button from "@material-ui/core/Button";
import "/workspace/sims-rooms-irl/src/front/styles/popover.css";
import SimsCard from "./simsCard";

const defaultRoomInfo = {id:null, name:"thisRoom", pic_url:"https://i.imgur.com/jG5GOPdh.png"};
export default function InteractiveRoom({id}) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [roomInfo, setRoomInfo] = useState(defaultRoomInfo);

  useEffect(async() => {
    const res = await fetch(
      "https://3001-valerieclai-simsroomsir-xyu3edngwba.ws-us89b.gitpod.io/api/rooms/" + id
    )
      const data = await res.json()

        setRoomInfo(data);
  }, [id]);

  return (
    <div className="container">
      <button title="List View" className="listBtn">
        <Link to={"/scholars_study/list"}>
          <div className="fa-solid fa-border-all fa-2xl"></div>
        </Link>
      </button>
      <h2 className="roomHeader">{roomInfo.name}</h2>
      <div className="roomBtnContainer">
        <img className="roomImg" src={roomInfo.pic_url} />
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
    </div>
  );
}
