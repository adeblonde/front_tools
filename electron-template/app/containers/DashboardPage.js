import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import DashboardWidget from '../components/DashboardWidget';
import * as DashboardActions from '../actions/counter';

function mapStateToProps(state) {
  return {
    counter: state.counter
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(DashboardActions, dispatch);
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(DashboardWidget);
