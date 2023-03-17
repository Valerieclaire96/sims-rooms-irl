import React, { useState, useEffect } from "react";
import Carousel from "../component/carousel";
import SimsCard from "../component/simsCard";
import { useParams } from "react-router-dom";
import { Widget } from '@typeform/embed-react'
const defaultRoomInfo = {
  id: null,
  name: "thisRoom",
  pic_url: "https://i.imgur.com/iaJefXz.png",
};

export const Home = ({}) => {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const { id } = useParams();
  const [roomInfoOne, setRoomInfoOne] = useState(defaultRoomInfo);
  const [roomInfoTwo, setRoomInfoTwo] = useState(defaultRoomInfo);
  const [roomInfoThree, setRoomInfoThree] = useState(defaultRoomInfo);
  const [roomInfoFour, setRoomInfoFour] = useState(defaultRoomInfo);
  const [roomInfoFive, setRoomInfoFive] = useState(defaultRoomInfo);
  const [objectList, setObjectList] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(
        process.env.BACKEND_URL + "/api/rooms/" + id == 2 || 6 || 10 || 4 || 8
      );
      const data = await res.json();
      setRoomInfoOne(data);
    }
    fetchData();
  }, [id]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(process.env.BACKEND_URL + "/api/rooms/6");
      const data = await res.json();

      setRoomInfoTwo(data);
    }
    fetchData();
  }, [id]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(process.env.BACKEND_URL + "/api/rooms/10");
      const data = await res.json();

      setRoomInfoThree(data);
    }
    fetchData();
  }, [id]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(process.env.BACKEND_URL + "/api/rooms/4");
      const data = await res.json();

      setRoomInfoFour(data);
    }
    fetchData();
  }, [id]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(process.env.BACKEND_URL + "/api/rooms/8");
      const data = await res.json();

      setRoomInfoFive(data);
    }
    fetchData();
  }, [id]);

  return (
    <div className="container mt-5 mb-3">
      <h1>
        Recreate Your Sim's Spaces <i>IRL</i>
      </h1>
      <Carousel
        sourceList={[
          roomInfoOne.pic_url,
          roomInfoTwo.pic_url,
          roomInfoThree.pic_url,
          roomInfoFour.pic_url,
          roomInfoFive.pic_url,
        ]}
      />
      <div className="d-flex mt-3 mb-3">
        {/* ask on how to make this better */}
        <SimsCard id={Math.floor(Math.random() * 68 + 1)} />
        <SimsCard id={Math.floor(Math.random() * 68 + 1)} />
        <SimsCard id={Math.floor(Math.random() * 68 + 1)} />
        <SimsCard id={Math.floor(Math.random() * 68 + 1)} />
      </div>
      
  <Widget id="https://fmx2klz7nhb.typeform.com/to/fBjrt8JT" style={{ width: '90%', height: "350px"}} className="my-form" />

    </div>
  );
};
