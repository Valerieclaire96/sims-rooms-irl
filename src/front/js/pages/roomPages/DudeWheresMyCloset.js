import React, { useState } from "react";
import { Link } from "react-router-dom";
import Featured from "../../component/featured";
import InteractiveRoom from "../../component/interactiveRoom.js";
import Popover from "@material-ui/core/Popover";
import Button from "@material-ui/core/Button";

export default function Dude({ cPic, cTitle, cPrice, cLink }) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);

  return (
    <div className="container">
      <InteractiveRoom />
      <Featured />
    </div>
  );
}
