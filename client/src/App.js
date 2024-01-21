import React, { useState, useEffect } from "react";

const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:4040/").then((event) => {
      console.log(event);
    });
  }, []);

  return (
    <div>
      <></>
    </div>
  );
};

export default App;
