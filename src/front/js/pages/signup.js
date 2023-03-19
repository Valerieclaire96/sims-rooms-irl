import React, { useState, useContext } from "react";
import "/workspace/sims-rooms-irl/src/front/styles/signup.css";
import { Context } from "../store/appContext";
import { useNavigate, Link } from "react-router-dom";


export default function Signup() {
  const { store, actions } = useContext(Context);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState(null);
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const token = sessionStorage.getItem("token");
  console.log(token);
  const handleClick = (e) => {
    e.preventDefault();
    console.log(e.target);
    actions.createUser(name, email, password).then((res) => navigate("/profile")).catch((err) => setError(err));
  }
    return (
        <>
        <form className="loginForm">
          <div className="loginFormContent">
            <h1>Create an Account</h1>
            <div className="input-field">
              <input
                className="myInput"
                type={"text"}
                placeholder={"Name"}
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </div>
            <div className="input-field">
              <input
                className="myInput"
                type={"text"}
                placeholder={"Email"}
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="input-field">
              <input
                className="myInput"
                type={"password"}
                placeholder={"Password"}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <Link className="link" to="/login">
              <span>Go Back</span>
            </Link>
            <br />
          </div>
          <div className="loginFormAction">
            {error && <div className="alert alert-danger">{error.msg || error.message || error}</div>}
            <button className="formBtn regBtn" onClick={(e) => handleClick(e)}>
              Register
            </button>
          </div>
        </form>
      </>
    );
  }