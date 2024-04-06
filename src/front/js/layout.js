import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { Home } from "./pages/home";
import Login from "./pages/login";
import Signup from "./pages/signup";
import Categories from "./pages/categories";
import Room from "./pages/room";
import Profile from "./pages/profile";
import AllObjects from "./pages/allObjects";
import Demo from "./pages/demo";
import Forgot from "./pages/forgotPassword";
import UpdatePassword from "./pages/updatePassword";
// import LoadingSpinner from "./component/loadingSpinnerjs";
import injectContext from "./store/appContext";

import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  return (
    <div>
      <BrowserRouter basename={basename}>
        <ScrollToTop>
          {/* <LoadingSpinner /> */}
          <Navbar />
          <Routes>
            <Route element={<Home />} path="/" />
            <Route element={<Login />} path="/login" />
            <Route element={<Signup />} path="/register" />
            <Route element={<Demo />} path="/demo" />
            <Route element={<Categories />} path="/categories" />
            <Route element={<Room />} path="/room/:id" />
            <Route element={<AllObjects />} path="/all-objects" />
            <Route element={<Categories />} path="/categories" /> 
            <Route element={<Profile />} path="/profile" />
            <Route element={<Forgot />} path="/forgot"/>
            <Route element={<UpdatePassword />} path='/update-password/token=:token' />
            <Route
              element={
                <img
                  className="cowPlant"
                  src="https://i.imgur.com/u01pV8K.png"
                  alt="404:PAGE NOT FOUND"
                />
              }
              path="*"
            />
          </Routes>
          <Footer />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

export default injectContext(Layout);
