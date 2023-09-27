const calculator = {};
calculator.add = (a, b) => a + b;
calculator.add(10,15)
calculator.subtract = (a, b) => a - b;
calculator.multiply = (a, b) => a * b;
calculator.divide = (a, b) => b !== 0 ? a / b : 'Cannot divide by zero!';
calculator.subtract(222, 122)
calculator.divide(222, 122)
calculator.multiply(222, 122)