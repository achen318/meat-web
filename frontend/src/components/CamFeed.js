import { useCallback, useEffect, useRef, useState } from 'react';

import Webcam from 'react-webcam';

const CamFeed = () => {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImgSrc(imageSrc);
  }, [webcamRef]);

  return (
    <>
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        height={600}
        width={600}
      />

      <button onClick={capture}>Capture photo</button>

      {/* {imgSrc && <img src={imgSrc} />} */}
    </>
  );
};

export default CamFeed;
