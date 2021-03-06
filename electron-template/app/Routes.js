/* eslint flowtype-errors/show-errors: 0 */
import React from 'react';
import { Switch, Route } from 'react-router';
import routes from './constants/routes';
import App from './containers/App';
import HomePage from './containers/HomePage';
import CounterPage from './containers/CounterPage';
import ChatbotPage from './containers/ChatbotPage';
import DashboardPage from './containers/DashboardPage';
import ApiPage from './containers/ApiPage';
import GridPage from './containers/GridPage';

export default () => (
  <App>
    <Switch>
      <Route path={routes.GRID} component={GridPage} />
      <Route path={routes.APISERVER} component={ApiPage} />
      <Route path={routes.DASHBOARD} component={DashboardPage} />
      <Route path={routes.CHATBOT} component={ChatbotPage} />
      <Route path={routes.COUNTER} component={CounterPage} />
      <Route path={routes.HOME} component={HomePage} />
    </Switch>
  </App>
);
