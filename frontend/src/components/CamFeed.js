import { useEffect, useRef, useState } from 'react';

import Webcam from 'react-webcam';

export default function CamFeed({ onFetched }) {
  const webcamRef = useRef(null);

  useEffect(() => {
    const timer = setInterval(() => {
      // get the img
      const imageSrc = webcamRef.current.getScreenshot();

      // send to backend (port 5000)
      fetch('http://localhost:5000/img-rec', {
        method: 'POST',
        body: imageSrc
      })
        .then((res) => res.json())
        .then((data) => onFetched(data))
        .catch((error) => console.error('Error:', error));
    }, 1000); // 1 second
    return () => clearInterval(timer);
  }, [webcamRef]);

  return (
    <Webcam
      ref={webcamRef}
      screenshotFormat="image/jpeg"
      height={600}
      width={600}
    />
  );
}
