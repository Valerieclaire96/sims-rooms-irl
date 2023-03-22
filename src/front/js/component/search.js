import algoliasearch from "algoliasearch/lite";
import React, { Component } from "react";
import {
  InstantSearch,
  Hits,
  SearchBox,
  Pagination,
  Highlight,
  ClearRefinements,
  RefinementList,
  Configure,
} from "react-instantsearch-dom";
import PropTypes from "prop-types";

const searchClient = algoliasearch(
  "PSIZSHJDSP",
  "dec39b29ff651d7927d7022f1ac8833b"
);

function Search() {
  return (
    <div className="ais-InstantSearch">
      <InstantSearch indexName="sims_irl_objects" searchClient={searchClient}>
        <div>
          <SearchBox />
          <Hits hitComponent={Hit} />
          <Pagination />
        </div>
      </InstantSearch>
    </div>
  );
}

function Hit(props) {
  return (
    <div className="card" style={{ width: "18rem" }}>
      <img
        src={props.hit.sims_pic_url}
        alt={props.hit.sims_name}
        className="card-img-top"
      />
      <div className="card-body">
        <h5 className="card-title mt-2" style={{ height: "60px" }}>
          {props.hit.sims_name + "- " + props.hit.price}
        </h5>
        <div className="cardBottom">
          <a href={props.hit.buy_url} target="blank">
            <button className="btn btn-info mb-2">Buy Now</button>
          </a>
          <button
            onClick={(e) => handleClick(e)}
            className="fa-sharp fa-regular fa-heart"
          ></button>
          {/* <FavoriteBtn  id={props.id} sims_card={props.sims_card}/> */}
        </div>
      </div>
    </div>
  );
}

Hit.propTypes = {
  hit: PropTypes.object.isRequired,
};

export default Search;
