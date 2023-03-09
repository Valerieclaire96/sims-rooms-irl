import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import Carousel from "../component/carousel";
import Featured from "../component/featured";

  // store.roomArr then store.roomArr.map loop through it eto get each value
// const { store, actions } = useContext(Context);
const defaultRoomInfo = {id:null, name:"thisRoom", pic_url:"https://i.imgur.com/jG5GOPdh.png"};

export const Home = ({id}) => {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [roomInfoOne, setRoomInfoOne] = useState(defaultRoomInfo);
  const [roomInfoTwo, setRoomInfoTwo] = useState(defaultRoomInfo);
  const [roomInfoThree, setRoomInfoThree] = useState(defaultRoomInfo);
  const [roomInfoFour, setRoomInfoFour] = useState(defaultRoomInfo);
  const [roomInfoFive, setRoomInfoFive] = useState(defaultRoomInfo);
  


  useEffect(() => {
    async function fetchData() {
    const res = await fetch(
      "https://3001-valerieclai-simsroomsir-xyu3edngwba.ws-us89b.gitpod.io/api/rooms/" +2  
    )
      const data = await res.json()

        setRoomInfoOne(data);
}; fetchData();
}, [id]);

useEffect(() => {
  async function fetchData() {
  const res = await fetch(
    "https://3001-valerieclai-simsroomsir-xyu3edngwba.ws-us89b.gitpod.io/api/rooms/8"
  )
    const data = await res.json()

      setRoomInfoTwo(data);
}; fetchData();
}, [id]);

useEffect(() => {
  async function fetchData() {
  const res = await fetch(
    "https://3001-valerieclai-simsroomsir-xyu3edngwba.ws-us89b.gitpod.io/api/rooms/10" 
  )
    const data = await res.json()

      setRoomInfoThree(data);
}; fetchData();
}, [id]);

useEffect(() => {
  async function fetchData() {
  const res = await fetch(
    "https://3001-valerieclai-simsroomsir-xyu3edngwba.ws-us89b.gitpod.io/api/rooms/4"  
  )
    const data = await res.json()

      setRoomInfoFour(data);
}; fetchData();
}, [id]);

useEffect(() => {
  async function fetchData() {
    const res = await fetch(
      "https://3001-valerieclai-simsroomsir-xyu3edngwba.ws-us89b.gitpod.io/api/rooms/8"  
    )
    const data = await res.json()

      setRoomInfoFive(data);
}; fetchData();
}, [id]);



  return (
    <div className="text-center mt-5 container">
      <h1>
        Recreate Your Sim's Spaces <i>IRL</i>
      </h1>
      <Carousel
        sourceList={[
          roomInfoOne.pic_url,
          roomInfoTwo.pic_url,
          roomInfoThree.pic_url,
          roomInfoFour.pic_url,
          roomInfoFive.pic_url
        ]}
      />
      {/* <Featured /> */}
    </div>
  );
};
