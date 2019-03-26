// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Api.css';
import routes from '../constants/routes';
import SwaggerUI, { presets } from 'swagger-ui';
// import styles from 'swagger-ui/dist/swagger-ui.css';

type Props = {
  increment: () => void,
  incrementIfOdd: () => void,
  incrementAsync: () => void,
  decrement: () => void,
  counter: number
};


class SwaggerTest extends Component {
	componentDidMount() {
	SwaggerUI({
		dom_id: '#swaggerContainer',
		url: `http://localhost:8080/v1/swagger.json`,
		presets: [presets.apis]
	  });
	}
  
	render() {
	  return (
		<div>
			<div className={styles.backButton} data-tid="backButton">
			<Link to={routes.HOME}>
				<i className="fa fa-arrow-left fa-3x" />
			</Link>
			</div>
			<div>
				<link rel="stylesheet" type="text/css" href="./components/swagger-ui.css" ></link>
				<div id="swaggerContainer">
				</div>
			</div>
		</div>
	  );
	}
  }
  
export default SwaggerTest;
