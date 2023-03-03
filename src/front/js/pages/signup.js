import React, { useState } from 'react';
import '/workspace/sims-rooms-irl/src/front/styles/signup.css';

// const SignupForm = () => {
//     const [username, setUsername] = useState('');
//     const [password, setPassword] = useState('');

//     const handleSubmit = (e) => {
//         e.preventDefault();

//         // Submit username/password here
//     }

//     return (
//         <form className="signupForm" onSubmit={handleSubmit}>
//             <input
//                 type="text"
//                 placeholder="Username"
//                 value={username}
//                 onChange={(e) => setUsername(e.target.value)}
//               />
//               <input
//                 type="password"
//                 placeholder="Password"
//                 value={password}
//                 onChange={(e) => setPassword(e.target.value)}
//               />
//               <button type="submit">Login</button>
//               <button type="submit">Register</button>
//        </form>
//     );
// };

class SignupForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: '',
            confirmPassword: ''
        };
    }
    
    handleChange = (name, value) => {
        this.setState({[name]: value});
    };
    
    render(){
        return (
            <div className="SignupForm">
                <label>
                    
                    <input type="text" name="username" onChange={(e) => this.handleChange('username', e.target.value)} 
                    placeholder="Signup"/>
                </label>
                <label>
                    <input type="password" name="password" onChange={(e) => this.handleChange('password', e.target.value)} 
                    placeholder="Password"/>
                </label>
                <label>
                    <input type="password" name="confirmPassword" onChange={(e) => this.handleChange('confirmPassword', e.target.value)} 
                    placeholder="Confirm Password"/>
                </label>
                <button className="primary-btn">Sign Up</button>
            </div>
        )
    }
}

export default SignupForm
