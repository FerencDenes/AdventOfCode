const md5 = require("js-md5");

const input = "ckczppom";
let i = 0;
while (!md5(input + i).startsWith("00000")) {
  i++;
}
console.log(i);
while (!md5(input + i).startsWith("000000")) {
  i++;
}
console.log(i);
