import React from 'react';

function JSONViewer({ data }) {
  return (
    <div>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default JSONViewer;
