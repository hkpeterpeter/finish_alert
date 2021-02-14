public class Say 
{
    public static void say(String m, String v) throws Exception {
        String cmd = "say -v " + v + " " + m;
        Runtime.getRuntime().exec(cmd).waitFor(); // wait until it finishes  
    }

    public static void main(String[] args) throws Exception {
        Say.say("Finish","Victoria");        // English
        Say.say("完了吧，如無意外", "Sin-ji"); // Cantonese
        Say.say("完結", "Ting-Ting");        // Chinese
        Say.say("終わり", "Kyoko");          // Japanese
        Say.say("종료", "Yuna");             // Korean
        Say.say("fin", "Monica");           // Spanish
        Say.say("finir", "Amelie");         // French        
    }
}