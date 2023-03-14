import React from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";


export const Navbar = () => {
  const [click, setClick] = React.useState(false);
  console.log(click);

  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary sticky-top">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">
          <img className="logo" src="https://i.imgur.com/4vATxe4.png" />
        </Link>
        <ul className="navbar-nav ml-auto mb-2 mb-lg-0">
          <li className="nav-item">
            <Link className="nav-link" to="/categories">
              All Rooms
            </Link>
          </li>
          <li className="nav-item ml-auto">
            <Link className="nav-link" to="/login">
              Login
            </Link>
          </li>
        </ul>
        <div className="search-bar">
          <input type="text" className="textbox" placeholder="search" />
          <div className="search-btn" href="#">
            <p>
              <img
                className="searchGif"
                src="http://images6.fanpop.com/image/photos/42800000/Plumbob-sims-4-42897071-365-750.gif"
              ></img>
            </p>
          </div>
        </div>
      </div>
    </nav>
  );
};
