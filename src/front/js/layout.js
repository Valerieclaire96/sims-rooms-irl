import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Home } from "./pages/home";
import  Login  from "./pages/login";
import  Signup from "./pages/signup";
import Categories from "./pages/categories";
import Dude from "./pages/roomPages/DudeWheresMyCloset";
import DudeList from "./component/roomList/dudeList";
import Lazy from "./pages/roomPages/lazySusansKitchen";
import LazyList from "./component/roomList/lazyList";
import Bites from "./pages/roomPages/QuickBitesLongTalks";
import BitesList from "./component/roomList/bitesList";
import Zzz from "./pages/roomPages/straightAsToZzz";
import ZzzList from "./component/roomList/aToZz";
import Sleep4geeks from "./pages/roomPages/sleep4geeks";
import GeeksList from "./component/roomList/geeksList";
import ScholarsStudy from "./pages/roomPages/scholarsStudy";
import ScholarsList from "./component/roomList/scholarsList";
import TweenageDirtbag from "./pages/roomPages/tweenageDirtbag";
import TweenageList from "./component/roomList/tweenageList";
import UnicornDreams from "./pages/roomPages/unicornDreams";
import UnicornList from "./component/roomList/unicornList";
import VroomRoom from "./pages/roomPages/vroomRoom";
import VroomList from "./component/roomList/vroomList";
import ZenDen from "./pages/roomPages/zenDen";
import ZenList from "./component/roomList/zenList";
import Demo from "./pages/demo";
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
                        <Route element={<Signup />} path="/register" />
                        <Route element={<Demo />} path="/demo" />
                        <Route element={<Categories />} path="/categories" />
                        <Route element={<Dude />} path="/dude_wheres_my_closet" />
                        <Route element={<DudeList />} path="/dude_list" />
                        <Route element={<Lazy />} path="/lazy_susans_kitchen" />
                        <Route element={<LazyList />} path="/lazy_susans_kitchen_list" />
                        <Route element={<Bites />} path="/quick_bites_long_talks" />
                        <Route element={<BitesList />} path="/quick_bites_long_talks_list" />
                        <Route element={<Zzz />} path="/straight_as_to_zzz" />
                        <Route element={<ZzzList />} path="/straight_as_to_zzz_list"/>
                        <Route element={<Sleep4geeks />} path="/sleep4geeks" />
                        <Route element={<GeeksList />} path="sleep4geeks/list" />
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
                        <Route element={<img src="https://i.imgur.com/u01pV8K.png" alt="404:PAGE NOT FOUND"/>} path="*" />
                        
                    </Routes>
                    <Footer />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
