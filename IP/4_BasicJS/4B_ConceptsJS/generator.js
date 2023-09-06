function* numberGenerator() {
    yield 1;
    yield 2;
    yield 3;
  }
  
  const gen = numberGenerator();
  
  console.log(gen.next());
  console.log(gen.next()); 
  console.log(gen.next()); 
  console.log(gen.next()); 
  