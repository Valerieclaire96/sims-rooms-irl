import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
  const [click, setClick] = React.useState(false);
  console.log(click);
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">
          <img
            className="logo"
            src="https://www.nicepng.com/png/detail/77-777209_the-sims-icon-triangle.png"
          />
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div
          className="collapse navbar-collapse flex-grow-0"
          id="navbarSupportedContent"
        >
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link className="nav-link" to="/">
                Categories
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/login">
                Login
              </Link>
            </li>
          </ul>
          <div class="search-bar">
            <input type="text" class="textbox" placeholder="search" />
            <div class="search-btn" href="#">
              <p>
                <img
                  className="searchGif"
                  src="http://images6.fanpop.com/image/photos/42800000/Plumbob-sims-4-42897071-365-750.gif"
                ></img>
              </p>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};
