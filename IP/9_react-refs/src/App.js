import React, { Component, forwardRef, useRef } from 'react';

const ChildComponent = forwardRef((props, ref) => {
  const inputRef = useRef(null);

  return (
    <div>
      <input type="text" ref={ref} />
    </div>
  );
});

class ParentComponent extends Component {
  constructor(props) {
    super(props);
    this.classRef = React.createRef(); 
    this.callbackRef = null; 
  }

  componentDidMount() {
    this.classRef.current.focus();
    if (this.callbackRef) {
      this.callbackRef.focus();
    }
  }

  setCallbackRef = (element) => {
    this.callbackRef = element; 
  };

  render() {
    return (
      <div>
        <h2>Accessing Refs in React</h2>
        <ChildComponent ref={this.classRef} /> 
        <ChildComponent ref={this.setCallbackRef} /> 
      </div>
    );
  }
}

function App() {
  const functionalRef = useRef();
  return (
    <div>
      <ParentComponent />
      <button onClick={() => functionalRef.current.focus()}>Focus Functional Ref</button>
      <ChildComponent ref={functionalRef} />
    </div>
  );
}

export default App;
