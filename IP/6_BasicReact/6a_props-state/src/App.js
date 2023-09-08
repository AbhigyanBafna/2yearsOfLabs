import React from 'react';
import './App.css';
import TodaysDate from './TodaysDate';
import DateTimeClass from './DateTimeClass';

function App() {
    const currentDate = new Date().toLocaleDateString();

    return (
        <div className="App">
            <TodaysDate currentDate={currentDate} />
            <DateTimeClass />
        </div>
    );
}

export default App;
