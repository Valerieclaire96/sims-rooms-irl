import React, { useState, useContext } from "react";
import "/workspace/sims-rooms-irl/src/front/styles/signup.css";
import { Context } from "../store/appContext";
import { useNavigate, Link } from "react-router-dom";


export default function Signup() {
  const { store, actions } = useContext(Context);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const token = sessionStorage.getItem("token");
  console.log(token);
  const handleClick = (e) => {
    e.preventDefault();
    console.log(e.target);
    actions.create_account(name, email, password);

    return (
      <div className="SignupForm">
        <form className="loginForm">
          <div className="loginFormContent">
            <h1>Login</h1>
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
            <Link className="link" to="/">
              <span>Continue without Loging in</span>
            </Link>
          </div>
          <div className="loginFormAction">
            <button className="formBtn regBtn" onClick={(e) => handleClick(e)}>
              Register
            </button>
          </div>
        </form>
      </div>
    );
  };
}

// export default function Signup() {
//   // constructor(props) {
//   //     super(props);
//   //     this.state = {
//   //         username: '',
//   //         password: '',
//   //         confirmPassword: ''
//   //     };
//   // }

//   // handleChange = (name, value) => {
//   //     this.setState({[name]: value});
//   // };
//   const { store, actions } = useContext(Context);
//   const [name, setName] = useState("");
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");

//   const token = sessionStorage.getItem("token");
//   console.log(token);
//   const handleClick = (e) => {
//     e.preventDefault();
//     console.log(e.target);
//     actions.create_account(name, email, password);

//     return (
//       <div className="SignupForm">
//         {/* <label>

//                     <input type="text" name="username" onChange={(e) => this.handleChange('username', e.target.value)}
//                     placeholder="Signup"/>
//                 </label>
//                 <label>
//                     <input type="password" name="password" onChange={(e) => this.handleChange('password', e.target.value)}
//                     placeholder="Password"/>
//                 </label>
//                 <label>
//                     <input type="password" name="confirmPassword" onChange={(e) => this.handleChange('confirmPassword', e.target.value)}
//                     placeholder="Confirm Password"/>
//                 </label>
//                 <button className="primary-btn">Sign Up</button> */}
//         <form className="loginForm">
//           <div className="loginFormContent">
//             <h1>Login</h1>
//             <div className="input-field">
//               <input
//                 className="myInput"
//                 type={"text"}
//                 placeholder={"Name"}
//                 value={name}
//                 onChange={(e) => setName(e.target.value)}
//               />
//             </div>
//             <div className="input-field">
//               <input
//                 className="myInput"
//                 type={"text"}
//                 placeholder={"Email"}
//                 value={email}
//                 onChange={(e) => setEmail(e.target.value)}
//               />
//             </div>
//             <div className="input-field">
//               <input
//                 className="myInput"
//                 type={"password"}
//                 placeholder={"Password"}
//                 value={password}
//                 onChange={(e) => setPassword(e.target.value)}
//               />
//             </div>
//             <Link className="link" to="/login">
//               <span>Go Back</span>
//             </Link>
//             <br />
//             <Link className="link" to="/">
//               <span>Continue without Loging in</span>
//             </Link>
//           </div>
//           <div className="loginFormAction">
//             <button className="formBtn regBtn" onClick={(e) => handleClick(e)}>
//               Register
//             </button>
//           </div>
//         </form>
//       </div>
//     )
//   };

//   // const SignupForm = () => {
//   //     const [username, setUsername] = useState('');
//   //     const [password, setPassword] = useState('');

//   //     const handleSubmit = (e) => {
//   //         e.preventDefault();

//   //         // Submit username/password here
//   //     }

//   //     return (
//   //         <form className="signupForm" onSubmit={handleSubmit}>
//   //             <input
//   //                 type="text"
//   //                 placeholder="Username"
//   //                 value={username}
//   //                 onChange={(e) => setUsername(e.target.value)}
//   //               />
//   //               <input
//   //                 type="password"
//   //                 placeholder="Password"
//   //                 value={password}
//   //                 onChange={(e) => setPassword(e.target.value)}
//   //               />
//   //               <button type="submit">Login</button>
//   //               <button type="submit">Register</button>
//   //        </form>
//   //     );
