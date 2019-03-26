require('../styles/ChatApp.css');

import React from 'react';
import io from 'socket.io-client';
import axios from 'axios';
import config from '../config';

import Messages from './Messages';
import ChatInput from './ChatInput';

class ChatApp extends React.Component {
  socket = {};
  connection = {};
  constructor(props) {
    super(props);
    this.state = { messages: [], answer: 'blank' };
	this.sendHandler = this.sendHandler.bind(this);
	
	// Test connection to the server
	axios.post(config.api + '/v1/answers', {
		id: 1,
		name: 'question',
		content: 'test_connection'
	})
    
    // Connect to the server
	// this.socket = io(config.api, { query: 'v1/models' }).connect();
	
    // this.socket = io(config.api, { query: `username=${props.username}` }).connect();

    // Listen for messages from the server
    // this.socket.on('server:message', message => {
    //   this.addMessage(message);
    // });
  }

  sendHandler(message) {
    const messageObject = {
      username: this.props.username,
      message
    };

    // Emit the message to the server
	// this.socket.emit('client:message', messageObject);
	var prepared_message = message.replace(' ','_');
	var res = axios.post(config.api + '/v1/answers', {
		id: 1,
		name: 'question',
		content: prepared_message
	}).then(response => {
		console.log(response.data);
		this.setState({answer: response.data});
	});

    messageObject.fromMe = true;
    this.addMessage(messageObject);

	// console.log(res.data);
	const messageAnswer = {
		username: 'AI',
		message: this.state.answer
	}
	messageAnswer.fromMe = false;
    this.addMessage(messageAnswer);
  }

  addMessage(message) {
    // Append the message to the component state
    const messages = this.state.messages;
    messages.push(message);
    this.setState({ messages });
  }

  render() {
    return (
      <div className="container">
        <h3>React Chat App</h3>
        <Messages messages={this.state.messages} />
        <ChatInput onSend={this.sendHandler} />
      </div>
    );
  }

}
ChatApp.defaultProps = {
  username: 'ML Padawan'
};

export default ChatApp;
