import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import Popover from "@material-ui/core/Popover";
import Button from "@material-ui/core/Button";
import RealCard from "./realObjectCard";

const defaultRoomInfo = {
  id: null,
  name: "thisRoom",
  pic_url: "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7d4d7c61-796e-421e-80f6-d565fd221647/d7nb9s6-d1a837cf-c615-44ed-9f8a-2224547dba6a.png/v1/fill/w_900,h_507,q_80,strp/sims_4_cas_inspired_wallpaper___plumbob_by_moozdeviant_d7nb9s6-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTA3IiwicGF0aCI6IlwvZlwvN2Q0ZDdjNjEtNzk2ZS00MjFlLTgwZjYtZDU2NWZkMjIxNjQ3XC9kN25iOXM2LWQxYTgzN2NmLWM2MTUtNDRlZC05ZjhhLTIyMjQ1NDdkYmE2YS5wbmciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0._jTWxHrCUgz7uz1Szr1-rgC26aBP8CL67dB57B3halM"
};
export default function InteractiveRoom({ id, objectList, setObjectList }) {
  const { store, actions } = useContext(Context);
  // console.log(store);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [open, setOpen] = React.useState(false);
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
      // console.log("//room objects by room id", data);
      setObjectList(data);
    }
    fetchData();
  }, [id]);

  return (
    <div className="container">
      <h2 className="roomHeader">{roomInfo.name}</h2>
      <div className="roomBtnContainer">
        <img className="roomImg" src={roomInfo.pic_url} />
        {objectList.length &&
          objectList.map((objectPlacement, index) => (
            <div>
              <Button
                className="roomBtn"
                key={roomInfo.name}
                style={{ left:objectPlacement.left, top: objectPlacement.top}}
                onClick={(event) => {
                  setObjectIndex(index);
                  // console.log(event.currentTarget);
                  setAnchorEl(event.currentTarget);
                  setOpen(true);
                }}
              >
                <div className="fa-regular fa-circle-dot fa-2xl"></div>
              </Button>
              {/* {console.log("hello from html", objectPlacement)} */}
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
          {objectList.length && (
            <RealCard id={objectList[objectIndex].object.id} />
          )}
        </Popover>
      </div>
    </div>
  );
}
