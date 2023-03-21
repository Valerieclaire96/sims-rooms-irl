import React from "react";

export default function UpdatePassword() {
  const [password, setPassword] = useState("");

  const token = sessionStorage.getItem("token");
  console.log(token);
  const handleClick = (e) => {
    e.preventDefault();
    console.log(e.target);
    actions
      .createUser(name, email, password)
      .then((res) => navigate("/profile"))
      .catch((err) => setError(err));
  };
  return (
    <div>
      <div>
        <form className="loginForm" onSubmit={handleSubmit}>
          <h1>New Password</h1>
          <div className="input-field">
            <input
              className="myInput"
              type={"password"}
              placeholder={"Password"}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  );
}
