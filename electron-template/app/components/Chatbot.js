// @flow
import React, { Component } from 'react';
import './Chatbot.css'
import { Link } from 'react-router-dom';
import styles from './Chatbot.css';
import routes from '../constants/routes';
import ChatApp from './chat_components/ChatApp';


export default class Chatbot extends Component<Props> {
	constructor(props) {
		super(props);
		this.state = { username: 'TestName' };
	}
	render() {
	return (
		<div>
		<link rel="stylesheet" type="text/css" href="./components/styles/ChatApp.css" ></link>
        <ChatApp username={this.state.username} />
		</div>
	  );
	}
}

// export default class Chatbot extends Component<Props> {
// 	state = {
// 		roomId: null,
// 		// currentUser: {},
// 		// currentRoom: {},
// 		messages: [],
// 		usersWhoAreTyping: [],
// 		joinableRooms: [],
// 		joinedRooms: [],
// 		text: '',
// 		loading: true
// 	  }
	
// 	//   componentDidMount() {
// 	// 	const chatManager = new Chatkit.ChatManager({
// 	// 	  instanceLocator: instanceLocator,
// 	// 	  userId: this.props.name,
// 	// 	  tokenProvider: new Chatkit.TokenProvider({
// 	// 		url: `${this.props.url}/authenticate`,
// 	// 	  }),
// 	// 	});
	
// 	// 	chatManager
// 	// 	  .connect()
// 	// 	  .then(currentUser => {
// 	// 		this.setState({ currentUser });
// 	// 		this.getRooms();
// 	// 	  })
// 	// 	  .catch(error => console.error('error', error));
// 	//   } 
	
// 	//   getRooms = () => {
// 	// 	this.state.currentUser.getJoinableRooms()
// 	// 	.then(joinableRooms => {
// 	// 		this.setState({
// 	// 			joinableRooms,
// 	// 			joinedRooms: this.state.currentUser.rooms,
// 	// 			loading: false
// 	// 		})
// 	// 	})
// 	// 	.catch(err => console.log('error on joinableRooms: ', err));
// 	//   }
	  
// 	  sendTypingEvent = () => {
// 		this.state.currentUser
// 		  .isTypingIn({ roomId: this.state.roomId })
// 		  .catch(error => console.error('error', error));
// 	  }
	
// 	  sendMessage = (text) => {
// 		this.state.currentUser.sendMessage({
// 		  text,
// 		  roomId: this.state.roomId,
// 		});
// 	  }
	
// 	  subscribeToRoom = (roomId) => {
// 		this.setState({ messages: [], loading: true });
// 		this.state.currentUser.subscribeToRoom({
// 			roomId: roomId,
// 			hooks: {
// 				onNewMessage: message => {
// 					this.setState({
// 						messages: [...this.state.messages, message],
// 						loading: false
// 					})
// 				},
// 				onUserStartedTyping: user => {
// 				  this.setState({
// 					usersWhoAreTyping: [...this.state.usersWhoAreTyping, user.name],
// 				  })
// 				},
// 				onUserStoppedTyping: user => {
// 				  this.setState({
// 					usersWhoAreTyping: this.state.usersWhoAreTyping.filter(
// 					  username => username !== user.name
// 					),
// 				  })
// 				},
// 			}
// 		})
// 		.then(room => {
// 			this.setState({
// 				roomId: roomId
// 			});
// 			this.getRooms();
// 		})
// 		.catch(err => console.log('error on subscribing to room: ', err));
// 	  }

//   render() {
//     const {joinableRooms, joinedRooms} = this.state;
//     return (
// 	<div>
// 		<link rel="stylesheet" type="text/css" href="./components/Chatbot.css" ></link>
//       <div className="app">
//         <RoomList
//           subscribeToRoom={this.subscribeToRoom}
//           rooms={[...joinableRooms, ...joinedRooms]}
//           logout={this.props.logout}
//           roomId={this.state.roomId} />
//         <MessageList 
//           roomId={this.state.roomId}
//           loading={this.state.loading}
//           messages={this.state.messages} />
//         <TypingIndicator usersWhoAreTyping={this.state.usersWhoAreTyping} />
//         <SendMessageForm
//           disabled={!this.state.roomId}
//           onSubmit={this.sendMessage}
//           onChange={this.sendTypingEvent} />
//       </div>
// 	  </div>
//     )
//   }
// }
