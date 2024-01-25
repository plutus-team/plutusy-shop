import React, { useState, useEffect } from "react";
import axios from "axios";
const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8000/test/").then((response) => {
      console.log(response);
    });
  }, []);

  return (
    <div>
      <></>
    </div>
  );
};

export default App;
