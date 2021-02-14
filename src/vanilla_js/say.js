function say(m = "Finish", v = "Victoria") {
   let synth = window.speechSynthesis;
   new Promise(
    function (resolve, reject) {
        let id = setInterval(() => {
            if (synth.getVoices().length !== 0) {
                resolve(synth.getVoices());
                clearInterval(id);
            }
        }, 10);
    }
   ).then((voices) => {
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