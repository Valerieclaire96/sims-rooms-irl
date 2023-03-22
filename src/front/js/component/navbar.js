import React, { useState, useContext } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import { Context } from "../store/appContext";

export const Navbar = () => {
  const [click, setClick] = React.useState(false);
  console.log(click);
  const { store, actions } = useContext(Context);

  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary sticky-top">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">
          <img className="logo" src="https://i.imgur.com/4vATxe4.png" />
        </Link>
        <img
          className="plumbobGif"
          src="http://images6.fanpop.com/image/photos/42800000/Plumbob-sims-4-42897071-365-750.gif"
        ></img>

        <ul className="navbar-nav ml-auto mb-2 mb-lg-0">
          {store.user && <li className="nav-item"><Link className="nav-link" to="/profile">Profile</Link></li>}
          <li className="nav-item">
            <Link className="nav-link" to="/categories">
              All Rooms
            </Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/all-objects">
              All Objects
            </Link>
          </li>
          {console.log("user", store.user)}

          <li className="nav-item ml-auto">
            {store.user ? (
              <span className="nav-link" to="/" onClick={() => {
                actions.logout();
              }}>
                Logout
              </span>
            ) : (
              <Link className="nav-link" to="/login">
                Login
              </Link>
            )}
          </li>
        </ul>
      </div>
    </nav>
  );
};
