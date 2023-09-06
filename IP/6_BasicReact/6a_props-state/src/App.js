import './App.css';
import TodaysDate from './TodaysDate';

function App() {

  const today = new Date();

  return (
    <div className="App">
      <h1>Hello World!</h1>
      <TodaysDate date={today} />
    </div>
  );
}

export default App;
