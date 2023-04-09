// import React, useState and useEffect hooks from 'react'
import React, { useState, useEffect } from 'react';
import './JSONViewer.css';

// define a functional component called JSONViewer
function JSONViewer() {
  // set up a state variable called data and a method to update it called setData
  const [data, setData] = useState(null);

  // use the useEffect hook to run a function once on mount
  useEffect(() => {
    // define an async function called fetchData
    async function fetchData() {
      // fetch the JSON data from the specified URL
      const response = await fetch('/output.json');
      // parse the response data into a JSON object
      const json = await response.json();
      // set the state variable data to the parsed JSON object
      setData(json);
    }

    // call the fetchData function
    fetchData();
  }, []);

  // return some JSX
  return (
    <div>
      {/* check if the data has been loaded */}
      {data ? (
        // if the data has been loaded, create a table
        <table>
          <thead>
            {/* create a table row for the table header */}
            <tr>
              {/* loop through the keys of the first item in the data array and create a table header cell for each one */}
              {Object.keys(data[0]).map((key, index) => (
                <th key={index}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {/* loop through each item in the data array and create a table row for each one */}
            {data.map((item, index) => (
              <tr key={index}>
                {/* loop through the values of each item in the data array and create a table cell for each one */}
                {Object.values(item).map((value, index) => (
                  <td key={index}>{value}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        // if the data has not been loaded yet, display a loading message
        <p>Loading...</p>
      )}
    </div>
  );
}

// export the JSONViewer component as a named export
export { JSONViewer };
