// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import routes from '../constants/routes';
import styles from './Home.css';

type Props = {};

export default class Home extends Component<Props> {
  props: Props;

  render() {
    return (
      <div className={styles.container} data-tid="container">
        <h2>Home</h2>
        <h3><Link to={routes.COUNTER} replace>to Counter</Link></h3>
        <h3><Link to={routes.CHATBOT} replace>to Chatbot</Link></h3>
        <h3><Link to={routes.APISERVER} replace>to Api Front</Link></h3>
        <h3><Link to={routes.DASHBOARD} replace>to Dashboard</Link></h3>
        <h3><Link to={routes.GRID} replace>to Grid Control Panel</Link></h3>
      </div>
    );
  }
}
