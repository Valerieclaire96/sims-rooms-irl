import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	const [click, setClick] = React.useState(false);
	console.log(click);
	return (
		<nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    <a className="navbar-brand" href="#"><img className="logo" src="https://www.nicepng.com/png/detail/77-777209_the-sims-icon-triangle.png"/></a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse flex-grow-0" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <Link className="nav-link" to="/">Categories</Link>
        </li>
		<li className="nav-item">
          <Link className="nav-link" to="/">Login</Link>
        </li>
      </ul>
      <form className="d-flex" role="search">
        <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button className="btn btn-outline-success" onClick={() => setClick(true)}>Search</button>
      </form>
    </div>
  </div>
</nav>
	);
};
