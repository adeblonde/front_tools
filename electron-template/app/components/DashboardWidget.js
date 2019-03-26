import React, { Component } from 'react';
import Dashboard from 'react-dazzle';

// Your widget. Just another react component.
// import CounterWidget from './widgets/CounterWidget';

// Widgets of the dashboard.
import BarChart from './widgets/BarChart';
import LineChart from './widgets/LineChart';
import DoughnutChart from './widgets/DoughnutChart';

// Default styles.
import 'react-dazzle/lib/style/style.css';

export default class DashboardWidget extends Component {
  constructor(props) {
	super(props);
    this.state = {      
		widgets: {
			EngineTelemetricsWidget: {
			  type: BarChart,
			  title: 'Engine',
			},
			PerformanceWidget: {
			  type: DoughnutChart,
			  title: 'Reactor Temp',
			},
			ShipVitalTelemetricsWidget: {
			  type: LineChart,
			  title: 'Reactor Telemetrics',
			},
	},
      // Layout of the dashboard
      layout: {
        rows: [{
          columns: [{
            className: 'col-md-12 col-sm-12 col-xs-12',
            widgets: [{key: 'ShipVitalTelemetricsWidget'}],
          }],
        }, {
          columns: [{
            className: 'col-md-8 col-sm-8 col-xs-8',
            widgets: [{key: 'EngineTelemetricsWidget'}],
          }, {
            className: 'col-md-4 col-sm-4 col-xs-4',
            widgets: [{key: 'PerformanceWidget'}],
          }],
        }],
      },
      editMode: false,
      isModalOpen: false,
      addWidgetOptions: null,
};
  }

  render() {
    return <Dashboard  widgets={this.state.widgets} layout={this.state.layout}  />
  }
}