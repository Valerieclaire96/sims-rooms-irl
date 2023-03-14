import algoliasearch from 'algoliasearch/lite';
import React, { Component } from 'react';
import {
  InstantSearch,
  Hits,
  SearchBox,
  Pagination,
  Highlight,
  ClearRefinements,
  RefinementList,
  Configure,
} from 'react-instantsearch-dom';
import PropTypes from 'prop-types';

const searchClient = algoliasearch(
  'PSIZSHJDSP',
  'dec39b29ff651d7927d7022f1ac8833b'
);

class Demo extends Component {
  render() {
    return (
      <div className="ais-InstantSearch">
        <InstantSearch indexName="sims_irl_objects" searchClient={searchClient}>
          <div className="right-panel">
            <SearchBox />
            <Hits hitComponent={Hit} />
            <Pagination />
          </div>
        </InstantSearch>
      </div>
    );
  }
}

function Hit(props) {
  return (
    <div>
      <img src={props.hit.sims_pic_url} align="left" alt={props.hit.sims_name} />
      <div className="hit-name"> {props.hit.sims_name}
      </div>
      <div className="hit-price">{props.hit.price}</div>
    </div>
  );
}

Hit.propTypes = {
  hit: PropTypes.object.isRequired,
};

export default Demo;