import './App.css';
import { useState } from 'react';
import axios from 'axios';


function App() {

  //store user input
  const [input, updateInput] = useState();

  //store flask answer
  const [answer, updateAnswer] = useState();

  const sendInput = async (event) => {
    if (event.key != "Enter") {
      return;
    }
    //send the input to the flask backend
    if (input != '') {  
      console.log('Input: ', input);
    }
  }


  return (
    <div className="App">
      <header className="App-header">
        <div className="chat-area">
            <input
              type="text"
              className="chat-input"
              placeholder="Input Question Here"
              onChange={(e) => updateInput(e.target.value)}
              onKeyDown={(e) => sendInput(e)}
          />
          <div className="chat-answer">
            <b>GenieConsultant:</b> answer answer answer answer answer answer
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
