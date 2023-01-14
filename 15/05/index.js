const fs = require("fs");
const { mainModule } = require("process");

const input = fs.readFileSync("05/input.txt").toString().trim().split("\n");

vowels = new Set(["a", "e", "i", "o", "u"]);

console.log(
  input.filter((str) => {
    let cnt = 0;
    let dbl = false;
    let prev = "";

    for (ch of str) {
      if (vowels.has(ch)) cnt++;
      if (prev === ch) {
        dbl = true;
      }
      prev = ch;
    }

    return (
      cnt >= 3 &&
      dbl &&
      str.indexOf("ab") === -1 &&
      str.indexOf("cd") === -1 &&
      str.indexOf("pq") === -1 &&
      str.indexOf("xy") === -1
    );
  }).length
);

console.log(
  input.filter((str) => {
    let singleRepeat = false;
    let doubleRepeat = false;

    for (let i = 0; i < str.length; i++) {
      singleRepeat |= i > 1 && str[i] == str[i - 2];
      const ss = str.substring(i - 2, i);
      doubleRepeat |= i > 1 && str.indexOf(str.substring(i - 2, i), i) !== -1;
    }

    return singleRepeat && doubleRepeat;
  }).length
);
