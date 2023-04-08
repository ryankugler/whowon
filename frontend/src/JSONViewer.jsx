import React, { useState, useEffect } from 'react';

function JSONViewer() {
  const [data, setData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('../backend/output.json');
      const json = await response.json();
      setData(json);
      console.log('JSON data:', json)
    }

    fetchData();
  }, []);

  return (
    <div>
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export {JSONViewer};