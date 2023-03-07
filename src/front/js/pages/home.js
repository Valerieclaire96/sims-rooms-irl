import React, { useContext } from "react";
import { Context } from "../store/appContext";
import Carousel from "../component/carousel";
import Featured from "../component/featured";

export const Home = () => {
  const { store, actions } = useContext(Context);

  // store.roomArr then store.roomArr.map loop through it eto get each value

  return (
    <div className="text-center mt-5 container">
      <h1>
        Recreate Your Sim's Spaces <i>IRL</i>
      </h1>
      {/* study, living, white bedroom, master bedroom, kitchen */}
      <Carousel
        sourceList={[
          "https://i.imgur.com/jG5GOPdh.png",
          "https://i.imgur.com/LbafRC5h.png",
          "https://i.imgur.com/8ahHHCQh.png",
          "https://i.imgur.com/SmhGAwI.png",
          "https://i.imgur.com/iLJ4Ura.png",
        ]}
      />
      <Featured />
    </div>
  );
};
