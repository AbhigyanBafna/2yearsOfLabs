
import React from 'react'

class TodaysDate extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  increment = () => {
    this.setState(prevCount => ({
      count: prevCount.count + 1
    }))
  }

  decrement = () => {
    this.setState(prevCount => ({
      count: prevCount.count - 1
    }))
  }

  render(){

    return (
      <div>
        {this.props.date.toString()}
        <h3 className='counter'>Count : {this.props.count}</h3>
        <button onClick={this.increment}>Increment </button>
        <button onClick={this.decrement}>Decrement </button>
        </div>
    );
  }

}

export default TodaysDate