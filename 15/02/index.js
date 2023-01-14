const fs = require("fs");
const { mainModule } = require("process");

const input = fs.readFileSync("02/input.txt").toString().trim().split("\n");
const re = RegExp("(.+)x(.+)x(.+)");
let part1 = 0;
let part2 = 0;
input.forEach((line) => {
  const match = line.trim().match(re);
  const valuesString = [match[1], match[2], match[3]];
  const values = valuesString.map((s) => parseInt(s));
  const tmp = [
    values[0] * values[1],
    values[2] * values[0],
    values[1] * values[2],
  ];
  tmp.sort(function (a, b) {
    return a - b;
  });
  values.sort(function (a, b) {
    return a - b;
  });
  part1 += 2 * (tmp[0] + tmp[1] + tmp[2]) + tmp[0];
  part2 += values[0] * values[1] * values[2] + 2 * (values[0] + values[1]);
});
console.log(part1);
console.log(part2);
