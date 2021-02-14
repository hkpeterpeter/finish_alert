
function setSpeech() {
    return new Promise(
        function (resolve, reject) {
            let synth = window.speechSynthesis;
            let id;
            id = setInterval(() => {
                if (synth.getVoices().length !== 0) {
                    resolve(synth.getVoices());
                    clearInterval(id);
                }
            }, 10);
        }
    )
}

function say(m = "Finish", v = "Victoria") {
   let synth = window.speechSynthesis;
   let s = setSpeech();
   s.then((voices) => {
        let utterThis = new SpeechSynthesisUtterance(m);
        for(i = 0; i < voices.length ; i++) {
            if(voices[i].name === v) {
                utterThis.voice = voices[i];
                break;
            }   
        } 
        synth.speak(utterThis);
   });  
}