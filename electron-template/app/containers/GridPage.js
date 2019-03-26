import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Grid from '../components/Grid';
import * as GridActions from '../actions/counter';

function mapStateToProps(state) {
  return {
    counter: state.counter
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(GridActions, dispatch);
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Grid);
