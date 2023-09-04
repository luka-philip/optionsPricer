import React from 'react';
import logo from './logo.svg';
import './App.css';
import OptionList from "./components/OptionsList";
import ProfitLossList from "./components/ProfitLossList";

function App() {
  return (
      <div className="App">
        <OptionList />
        <ProfitLossList />
      </div>
  );
}

export default App;
