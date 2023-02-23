import React, { useContext } from "react";
import { Context } from "../store/appContext";
import Carousel from "../component/carousel";
import HomeCards from "../component/homeCards";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5 container">
			{/* study, living, white bedroom, master bedroom, kitchen */}
			<Carousel sourceList={["https://i.imgur.com/jG5GOPdh.png","https://i.imgur.com/LbafRC5h.png","https://i.imgur.com/8ahHHCQh.png","https://i.imgur.com/SmhGAwI.png","https://i.imgur.com/iLJ4Ura.png"]}/>
			<HomeCards />
		</div>
	);
};