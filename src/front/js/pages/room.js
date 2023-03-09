import React, { useState } from "react";
import { Link } from "react-router-dom";
import Featured from "../component/featured";
import InteractiveRoom from "../component/interactiveRoom.js";
import Popover from "@material-ui/core/Popover";
import Button from "@material-ui/core/Button";
import { useParams } from "react-router-dom";

export default function Room({}) {
  const { id } = useParams();
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);

  return (
    <div className="container">
      <InteractiveRoom id={id} />
      <Featured />
    </div>
  );
}
