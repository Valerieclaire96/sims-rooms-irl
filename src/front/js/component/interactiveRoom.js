import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import Popover from "@material-ui/core/Popover";
import Button from "@material-ui/core/Button";
import RealCard from "./realObjectCard";

const defaultRoomInfo = {
  id: null,
  name: "thisRoom",
  pic_url: "https://i.imgur.com/jG5GOPdh.png",
};
export default function InteractiveRoom({ id, objectList, setObjectList }) {
  const { store, actions } = useContext(Context);
  console.log(store);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [open, setOpen ]= React.useState(false);
  const [roomInfo, setRoomInfo] = useState(defaultRoomInfo);
  const [objectIndex, setObjectIndex] = useState(0);
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
      <h2 className="roomHeader">{roomInfo.name}</h2>
      <div className="roomBtnContainer">
        <img className="roomImg" src={roomInfo.pic_url} />
        {objectList.length && objectList.map((objectPlacement, index) => (
          <div>
            <Button
              className="roomBtn"
              style={{ left: objectPlacement.left, top: objectPlacement.top }}
              onClick={(event) => {
                setObjectIndex(index);
                console.log(event.currentTarget);
                setAnchorEl(event.currentTarget);
                setOpen(true);
              }}
            >
              <div className="fa-regular fa-circle-dot fa-2xl"></div>
            </Button>  
            {console.log("hello from html" ,objectPlacement)}
            </div>
            ))}
            <Popover
              anchorEl={anchorEl}
              open={open}
              id={open ? "simple-popover" : undefined}
              onClose={() => {
                setOpen(false);
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
              {objectList.length && <RealCard id={(objectList[objectIndex].object.id)} />}
            </Popover>
      </div>
    </div>
  );
}
