import React, { Component } from 'react';

class DateTimeClass extends Component {
    constructor(props) {
        super(props);
        this.state = {
            dateTime: '',
            font: '',
            color: '',
        };
    }

    displayDateTime = () => {
        let currentDateTime = new Date().toLocaleString();
        this.setState({
            dateTime: currentDateTime,
            font: 'Comic Sans MS',
            color: 'blue',
        });
    };

    render() {
        return (
            <div style={{ fontFamily: this.state.font || 'Arial', color: this.state.color || 'black' }}>
                <h2>{this.state.dateTime}</h2>
                <button onClick={this.displayDateTime}>Display Date & Time</button>
            </div>
        );
    }
}

export default DateTimeClass;

