import React, { useState } from "react";
import { Link } from "react-router-dom";
import Featured from "../../component/featured";
import InteractiveRoom from "../../component/interactiveRoom.js";

export default function TweenageDirtbag({ cPic, cTitle, cPrice, cLink }) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);

  return (
    <div className="container">
      <InteractiveRoom />
      <Featured />
    </div>
  );
}
