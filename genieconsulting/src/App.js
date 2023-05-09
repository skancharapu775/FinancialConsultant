import './App.css';
import { useState } from 'react';
import axios from 'axios';


function App() {

  //store user input
  const [input, updateInput] = useState({
    input: ''
  })

  //store flask answer
  const [answer, updateAnswer] = useState("Hello, I am GenieConsultant, ask any question regarding investing or finances");
  


  const sendInput = async (event) => {
    if (event.key != "Enter") {
      return;
    }
    //send the input to the flask backend
    if (input != '') {  
      console.log('Input: ', input);
      updateAnswer("Loading answer...");

    //silly post request, untested as of 5/5/23
    axios.post('http://localhost:5000/consultant', input)
      .then(res => {
          axios.get('http://localhost:5000/consultant')
        .then(res => {
          updateAnswer(res.data)
        })
      })
      .catch(err => {
        console.log(err)
      })
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
              onChange={(e) => updateInput({
                ...input,
                input: e.target.value
              })}
              onKeyDown={(e) => sendInput(e)}
          />
          <div className="chat-answer">
            {answer}
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
