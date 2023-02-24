import React, { useState } from 'react';
import '/workspace/sims-rooms-irl/src/front/styles/loginform.css';


const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();

        // Submit username/password here
    }

    return (
        <form className="loginForm" onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <button type="submit">Login</button>
              <button type="submit">Register</button>
       </form>
    );
};

export default LoginForm;
