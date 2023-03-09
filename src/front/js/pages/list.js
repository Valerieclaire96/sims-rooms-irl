import React, { useState, useEffect } from "react";
import SimsCard from "../component/simsCard";
import RealCard from "../component/realObjectCard";
import { Route } from "react-router-dom";

// i am going to need to loop through how many objects as room has and make it create divs as needed
export default function List() {
  return <div className="container">
          <div className="row">
            <SimsCard />
            <RealCard />
          </div>
    </div>;
}
