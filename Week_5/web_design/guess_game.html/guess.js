const randomnumbers =  math.floar (math.random()=100) 
let attempts = 0
function checkGuess(){
    const guess = parseInt(document.getElementById("guessfield").value)
    attempt ++ ;
    if(isNaN(guess)|| guess < 1|| guess > 100  ){
        setmessage ("Please eneter a valid number between 1 and 100")
        return;
    }
    if(guess === randomnumbers){
        setmessage("congradulations Guessed correcly")
        document.getElementById("guessfield")
    }else if ( guess < randomnumber){
        setmessage("too low try again")
    }else{
        setmessage("too high  try again")
    }
}
function setmessage(message){
    document.getElementById("message").textContent = message;
}