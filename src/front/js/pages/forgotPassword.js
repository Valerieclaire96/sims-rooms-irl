import React from "react";

const token = sessionStorage.getItem("token");
console.log(token);
const handleSubmit = async (e) => {
  e.preventDefault();
  const opts = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const res = await fetch(process.env.BACKEND_URL + "/api/user", opts);
  if (res.status < 200 || res.status >= 300) {
    throw new Error("There was an error signing in");
  }
  const data = await res.json();
};

export default function Forgot() {
  return (
    <div>
      <form className="loginForm" onSubmit={handleSubmit}>
        <h1>Email</h1>
        <input
          type={"text"}
          placeholder="email"
          value={email}
          onChange={(e) => setemail(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
