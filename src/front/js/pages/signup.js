import React from 'react';
import '/workspace/sims-rooms-irl/src/front/styles/signup.css';
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
                <h1 className="H1-Signup">Register</h1>
                <label>Username:
                    <input type="text" name="username" onChange={(e) => this.handleChange('username', e.target.value)} />
                </label>
                <label>Password:
                    <input type="password" name="password" onChange={(e) => this.handleChange('password', e.target.value)} />
                </label>
                <label>Confirm Password:
                    <input type="password" name="confirmPassword" onChange={(e) => this.handleChange('confirmPassword', e.target.value)} />
                </label>
                <button className="primary-btn">Sign Up</button>
            </div>
        )
    }
}

export default SignupForm
