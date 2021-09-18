import React, {useState} from 'react'

import FileDropZone from './FileDropZone';
import Thread from './Thread';

import './App.css';

function App() {
  const [loaded, setLoaded] = useState(false)
  const [entries, setEntries] = useState([])

  return (
    <div className="App">
      {!loaded && <FileDropZone onResult={result => {
        setEntries(result)
        setLoaded(true)
      }}/>}

      {loaded && <Thread entries={entries} />}
    </div>
  );
}

export default App;
