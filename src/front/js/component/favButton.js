import React, { useContext } from "react";
import { Context } from "../store/appContext";


export default function FavoriteBtn(props) {
  const { store, actions } = useContext(Context);
  const handleClick = (e) => {
    if (
      document.querySelector(`#favIcon${props.sims_card}${props.id}`).classList ==
      "far fa-heart"
    ) {
      document.querySelector(`#favIcon${props.sims_card}${props.id}`).classList =
        "fas fa-heart";
    } else {
      document.querySelector(`#favIcon${props.sims_card}${props.id}`).classList =
        "far fa-heart";
    }
    // console.log(props.item);
    let fav = {
      id: props.id,
      sims_card: props.sims_card,
    };
    if (
      store.favorites.filter(
        (e) => e.id === props.id && e.sims_card === props.sims_card
      ).length > 0
    ) {
      // remove
      console.log("here");
      actions.removeFavorite(fav);
    } else {
      // add
      actions.addFavorite(fav);
    }
  };
  return (
    <div>
      <button style={{justifyContent:"flex-end", backgroundColor: "transparent", outline: "none", border:"none"}} onClick={(e) => handleClick(e)}>
        <i id={`favIcon${props.sims_card}${props.id}`} className="far fa-heart" />
      </button>
    </div>
  );
}
