let voices = []; // store the voices
let synth = window.speechSynthesis;

function say(m = "Finish", v = "Victoria") {
    const speak = () => {
        let utterThis = new SpeechSynthesisUtterance(m);
        for ( let voice of voices ) {
            if ( voice.name === v ) {
                utterThis.voice = voice;
                break;
            }
        }
        synth.speak(utterThis);
    }
    if ( voices.length === 0 ) {  // For the first time without a voice list
        // Note: synth.getVoices() - use setInterval trick to get the voice list from the server
        let id = setInterval(() => {
            voices = synth.getVoices();
            if (voices.length !== 0) {
                clearInterval(id);
                speak();
            }
        }, 10);
    } 
    else { // call the speak() handler if the voice list is ready
        speak();
    }
}