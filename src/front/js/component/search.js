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
        <div className="hit-name mt-2">
          {" "}
          {props.hit.sims_name}
          <br></br>
          {props.hit.price}
          <div className="hit-price"></div>
          <div className="cardBottom">
            <a href={props.hit.buy_url} target="blank">
              <button className="btn btn-primary mt-2">Buy Now</button>
            </a>
            <div className="fa-sharp fa-regular fa-heart"></div>
          </div>
        </div>
      </div>
    </div>
  );
}

Hit.propTypes = {
  hit: PropTypes.object.isRequired,
};

export default Search;
