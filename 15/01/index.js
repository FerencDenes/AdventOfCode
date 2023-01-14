const fs = require("fs");

const input = fs.readFileSync("01/input.txt").toString().trim();
let res2;

console.log(
  [...input].reduce((acc, ch, index) => {
    if (ch === ")") acc--;
    if (ch === "(") acc++;
    if (!res2 && acc === -1) {
      res2 = index + 1;
    }
    return acc;
  }, 0)
);

console.log(res2);
