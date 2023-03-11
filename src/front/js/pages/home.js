import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import Carousel from "../component/carousel";
import SimsCard from "../component/simsCard";
import { useParams } from "react-router-dom";

  // store.roomArr then store.roomArr.map loop through it eto get each value
// const { store, actions } = useContext(Context);
const defaultRoomInfo = {id:null, name:"thisRoom", pic_url:"https://i.imgur.com/iaJefXz.png"};
const defaultSimsObjectInfo = {id:null, name:"thisObject", sims_names:"thisCard", sims_pic_url:"https://i.imgur.com/ZDVzExF.png", buy_url: "https://a.co/d/8WBBavf", price:16}

export const Home = ({}) => {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const { id } = useParams();
  const [ objectInfo, setObjectInfo] = useState(defaultSimsObjectInfo);
  const [roomInfoOne, setRoomInfoOne] = useState(defaultRoomInfo);
  const [roomInfoTwo, setRoomInfoTwo] = useState(defaultRoomInfo);
  const [roomInfoThree, setRoomInfoThree] = useState(defaultRoomInfo);
  const [roomInfoFour, setRoomInfoFour] = useState(defaultRoomInfo);
  const [roomInfoFive, setRoomInfoFive] = useState(defaultRoomInfo);
  


useEffect(() => {
    async function fetchData() {
    const res = await fetch(
      process.env.BACKEND_URL + "/api/rooms/2" ,  
    )
      const data = await res.json()
        setRoomInfoOne(data);
}; fetchData();
}, [id]);

useEffect(() => {
  async function fetchData() {
  const res = await fetch(
    process.env.BACKEND_URL + "/api/rooms/6"
  )
    const data = await res.json()

      setRoomInfoTwo(data);
}; fetchData();
}, [id]);

useEffect(() => {
  async function fetchData() {
  const res = await fetch(
    process.env.BACKEND_URL + "/api/rooms/10" 
  )
    const data = await res.json()

      setRoomInfoThree(data);
}; fetchData();
}, [id]);

useEffect(() => {
  async function fetchData() {
  const res = await fetch(
    process.env.BACKEND_URL + "/api/rooms/4"  
  )
    const data = await res.json()

      setRoomInfoFour(data);
}; fetchData();
}, [id]);

useEffect(() => {
  async function fetchData() {
    const res = await fetch(
      process.env.BACKEND_URL + "/api/rooms/8"  
    )
    const data = await res.json()

      setRoomInfoFive(data);
}; fetchData();
}, [id]);


useEffect(() => {
  async function fetchData() {
    const res = await fetch(
      process.env.BACKEND_URL + "/api/objects"  
    )
    const data = await res.json()

      setObjectsInfo(data);
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
      <div className="cardContainerMain">
      <SimsCard id={5}/>
      <SimsCard id={50}/>
      <SimsCard id={14}/>
      <SimsCard id={29}/>
      </div>
    </div>
  );
};
