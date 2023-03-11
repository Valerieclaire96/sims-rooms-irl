import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import Popover from "@material-ui/core/Popover";
import Button from "@material-ui/core/Button";
import "/workspace/sims-rooms-irl/src/front/styles/popover.css";
import RealCard from "./realObjectCard";

const defaultRoomInfo = {
  id: null,
  name: "thisRoom",
  pic_url: "https://i.imgur.com/jG5GOPdh.png",
};
export default function InteractiveRoom({ id }) {
  const { store, actions } = useContext(Context);
  console.log(store);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [roomInfo, setRoomInfo] = useState(defaultRoomInfo);
  const [objectList, setObjectList] = useState([]);
  // const roomInfo = store.roomArr.find((room) => room.id === id);
  // console.log(roomInfo)
  useEffect(() => {
    async function fetchData() {
      const res = await fetch(process.env.BACKEND_URL + "/api/rooms/" + id);
      const data = await res.json();

      setRoomInfo(data);
    }
    fetchData();
  }, [id]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(
        process.env.BACKEND_URL + "/api/room/" + id + "/objects/"
      );
      const data = await res.json();
      console.log("//room objects by room id", data);
      setObjectList(data);
    }
    fetchData();
  }, [id]);

  return (
    <div className="container">
      {/* <button title="List View" className="listBtn">
        <Link to={"/scholars_study/list"}>
          <div className="fa-solid fa-border-all fa-2xl"></div>
        </Link>
      </button> */}
      <h2 className="roomHeader">{roomInfo.name}</h2>
      <div className="roomBtnContainer">
        <img className="roomImg" src={roomInfo.pic_url} />
        {objectList.map((objectPlacement) => (
          <div>
            <Button
              className="studyBtn"
              style={{ left: objectPlacement.left, top: objectPlacement.top }}
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
              <RealCard id={(objectPlacement.object.id)} />
            </Popover>
          </div>
        ))}
        {/* <Button
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
        </Popover>*/}
      </div>
    </div>
  );
}
