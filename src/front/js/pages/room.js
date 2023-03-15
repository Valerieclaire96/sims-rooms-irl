import React, { useState } from "react";
import InteractiveRoom from "../component/interactiveRoom.js";
import { useParams } from "react-router-dom";
import RealCard from "../component/realObjectCard";

export default function Room({}) {
  const { id } = useParams();
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [objectList, setObjectList] = useState([]);


  return (
    <div className="container mt-5">
      <InteractiveRoom id={id} objectList={objectList} setObjectList={setObjectList} />
      <div className="d-flex col-10 overflow-auto mt-5" >
      {objectList.map((objectPlacement, objectIndex) => {
        return objectList.length && <RealCard id={(objectList[objectIndex].object.id)} key={objectIndex} />
      })}
      </div>
    </div>
  );
}
