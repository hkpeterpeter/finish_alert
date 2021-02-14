// By default, Javascript runs in a parallel (async/await is needed)
const util = require('util');
const exec = util.promisify(require('child_process').exec);
async function say(m = "Finish", v = "Victoria") {
  await exec(`say -v ${v} ${m}`) 
}

// Without async/await, all sentences will be spoken at the same time
async function main() {
  await say()                              // English
  await say(m="完了吧，如無意外",v="Sin-ji")  // Cantonese
  await say(m="完結",v="Ting-Ting")         // Chinese
  await say(m="終わり",v="Kyoko")           // Japanese
  await say(m="종료",v="Yuna")              // Korean
  await say(m="fin",v="Monica")            // Spanish
  await say(m="finir",v="Amelie")          // French
}
main()

