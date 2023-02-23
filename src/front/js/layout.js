import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Home } from "./pages/home";
import  Login  from "./pages/login";
import Categories from "./pages/categories";
import Geeks4sleep from "./pages/geeks4sleep";
import GeeksList from "./component/geeksList";
import ScholarsStudy from "./pages/scholarsStudy";
import ScholarsList from "./component/scholarsList";
import TweenageDirtbag from "./pages/tweenageDirtbag";
import TweenageList from "./component/tweenageList";
import UnicornDreams from "./pages/unicornDreams";
import UnicornList from "./component/unicornList";
import VroomRoom from "./pages/vroomRoom";
import VroomList from "./component/vroomList";
import ZenDen from "./pages/zenDen";
import ZenList from "./component/zenList";
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
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />
                        <Route element={<Login />} path="/login" />
                        <Route element={<Geeks4sleep />} path="/geeks4sleep" />
                        <Route element={<GeeksList />} path="geeks4sleep/list" />
                        <Route element={<ScholarsStudy />} path="/scholars_study" />
                        <Route element={<ScholarsList />} path="/scholars_study/list" />
                        <Route element={<TweenageDirtbag />} path="/tweenage_dirtbag" />
                        <Route element={<TweenageList />} path="/tweenageList" />
                        <Route element={<UnicornDreams />} path="/unicorn_dream" />
                        <Route element={<UnicornList />} path="/unicornList" />
                        <Route element={<VroomRoom />} path="/vroom_room" />
                        <Route element={<VroomList />} path="/vroomList" />
                        <Route element={<ZenDen />} path="/zen_den" />
                        <Route element={<ZenList />} path="/zenList" />
                        <Route element={<Categories />} path="/categories" />
                        <Route element={<h1>Not found!</h1>} />
                        
                    </Routes>
                    <Footer />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
