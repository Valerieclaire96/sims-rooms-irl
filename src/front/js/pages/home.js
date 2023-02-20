import React, { useContext } from "react";
import { Context } from "../store/appContext";
import Carousel from "../component/carousel";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<Carousel sourceList={["https://picsum.photos/id/22/2000/1000","https://picsum.photos/id/21/2000/1000","https://picsum.photos/id/23/2000/1000"]}/>
		</div>
	);
};
