function changebg(){
    const colors = ["red", "blue", "purple", "brown"];
    const randomColor = Math.floor(Math.random() * colors.length);
    document.body.style.backgroundColor = colors[randomColor];
}

setInterval(changebg, 500);