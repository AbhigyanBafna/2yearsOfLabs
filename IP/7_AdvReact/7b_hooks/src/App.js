import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputValue1, setInputValue1] = useState('');
  const [inputValue2, setInputValue2] = useState('');

  return (
    <div className="App">
      <header className="App-header">
        
        <h3>Box 1</h3>
        <input 
          type="text"
          value={inputValue1}
          onChange={(e) => setInputValue1(e.target.value)}
        />

        <h3>Box 2</h3>
        <input 
          type="text"
          value={inputValue2}
          onChange={(e) => setInputValue2(e.target.value)}
        />
        <p>{inputValue1} {inputValue2}</p>

      </header>
    </div>
  );
}

export default App;
