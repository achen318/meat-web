import Webcam from 'react-webcam';

const CamFeed = () => {
  return (
    <div className="container">
      <Webcam height={600} width={600} />
    </div>
  );
};

export default CamFeed;

// https://blog.logrocket.com/using-react-webcam-capture-display-images/
