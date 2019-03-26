import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Chatbot from '../components/Chatbot';
import * as ChatbotActions from '../actions/counter';

function mapStateToProps(state) {
  return {
    counter: state.counter
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(ChatbotActions, dispatch);
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Chatbot);
