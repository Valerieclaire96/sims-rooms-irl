import React from "react";
import { Link } from "react-router-dom";

export default function Carousel({ sourceList }) {
  const [index, setIndex] = React.useState(0);

  return (
    <div className="carousel container slide">
      <div className="carousel-indicators">
        {sourceList.map((url, currentIndex) => (
          <button
            onClick={() => setIndex(currentIndex)}
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
        {sourceList.map((url, currentIndex) => (
          <div
            className={
              "carousel-item "  + (index === currentIndex ? "active" : "")
            }
          >
            <Link to={index == 0 ? "/scholars_study" : index == 1 ? "/scholars_study": index == 2 ? "/scholars_study" : index == 3 ? "/scholars_study": "/scholars_study"}><img src={url} className="carousel-room d-block w-100" /></Link>
          </div>
        ))}
      </div>
      <button
        onClick={() =>
          setIndex(index === 0 ? sourceList.length - 1 : index - 1)
        }
        className="carousel-control-prev"
        type="button" 
        data-bs-target="#carouselExampleIndicators" data-bs-slide="prev"
      >
        <span className="carousel-control-prev-icon" aria-hidden="true" ></span>
        <span className="visually-hidden">Previous</span>
      </button>
      <button
        onClick={() =>
          setIndex(index === sourceList.length - 1 ? 0 : index + 1)
        }
        className="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleIndicators" data-bs-slide="next"
      >
        <span className="carousel-control-next-icon" aria-hidden="true"></span>
        <span className="visually-hidden">Next</span>
      </button>
    </div>
  );
}
