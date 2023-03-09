import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { TransitionGroup, CSSTransition } from "react-transition-group";

export default function Carousel({ sourceList }) {
  const [index, setIndex] = React.useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((index) => (index + 1) % sourceList.length);
    }, 5500);
    return () => clearInterval(interval);
  },[]);

  return (
    <div className="carousel slide" data-ride="carousel">
      <div className="carousel-indicators">
        {sourceList.map((url, currentIndex) => (
          <button
            onClick={() => setIndex(currentIndex) && setInterval(5500)}
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide-to={currentIndex}
            className={index === currentIndex ? "active" : ""}
            aria-current="true"
            aria-label={"Slide " + (index + 1)}
          ></button>
        ))}
      </div>
      <div className="carousel-inner">
        <TransitionGroup>
          <CSSTransition
            key={sourceList[index]}
            timeout={3500}
            classNames="slide-right"
          >
            <div>
              {sourceList.map((url, currentIndex) => (
                <div
                  className={
                    "carousel-item " + (index === currentIndex ? "active" : "")
                  }
                >
                  <Link
                    to={
                      index == 0
                        ? "room/2"
                        : index == 1
                        ? "/room/6"
                        : index == 2
                        ? "/room/10"
                        : index == 3
                        ? "/room/4"
                        :"/room/8"
                    }
                  >
                    <img src={url} className="carousel-room d-block w-100" />
                  </Link>
                </div>
              ))}
            </div>
          </CSSTransition>
        </TransitionGroup>

        <button
          onClick={() =>
            setIndex(index === 0 ? sourceList.length - 1 : index - 1)
          }
          className="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleIndicators"
          data-bs-slide="prev"
        >
          <span
            className="carousel-control-prev-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button
          onClick={() =>
            setIndex(index === sourceList.length - 1 ? 0 : index + 1)
          }
          className="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleIndicators"
          data-bs-slide="next"
        >
          <span
            className="carousel-control-next-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  );
}
