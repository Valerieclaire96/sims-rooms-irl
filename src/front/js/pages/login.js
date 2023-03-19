import React, { useState, useContext  } from 'react';
import '/workspace/sims-rooms-irl/src/front/styles/loginform.css';
import { Context } from "../store/appContext";
import { useNavigate, Link } from 'react-router-dom';


export default function Login() {
    const [email, setemail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const { store, actions } = useContext(Context);
    const navigate = useNavigate();

    const token = sessionStorage.getItem("token");
    console.log(token);
    const handleSubmit = (e) => {
        e.preventDefault();
        actions.login(email, password).then((res) => navigate("/profile")).catch((err) => setError(err));
        // Submit email/password here
    }

    return (
        <form className="loginForm" onSubmit={handleSubmit}>
            <h1>Login</h1>
            <input
                type={"text"}
                placeholder="email"
                value={email}
                onChange={(e) => setemail(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit">Login</button>
            <button><Link to="/register">Register</Link></button>
    </form>
    );
};

