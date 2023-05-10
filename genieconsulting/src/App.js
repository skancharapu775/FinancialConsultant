import './App.css';
import { useState } from 'react';
import axios from 'axios';
import Header from './components/Header.js'
import { Button } from '@mui/material';


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
      <Header />
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
        <a className="url-button" href="http://localhost:5000/pdf" target="_blank" download="Financial_Plan.pdf">
            <Button variant="contained">Download PDF</Button>
        </a>
      </header>
    </div>
  );
}

export default App;
