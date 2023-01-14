const fs = require("fs");
const _ = require("lodash");
const { mainModule } = require("process");

const input = fs.readFileSync("06/input.txt").toString().trim().split("\n");

const arr = new Array(1000).fill().map((a) => new Array(1000).fill(false));
const arr2 = new Array(1000).fill().map((a) => new Array(1000).fill(0));

const re = RegExp("^(.*) (\\d+),(\\d+) through (\\d+),(\\d+)$");

const operate = (x0, y0, x1, y1, pred, pred2) => {
  for (let i = parseInt(x0); i <= parseInt(x1); i++) {
    for (let j = parseInt(y0); j <= parseInt(y1); j++) {
      arr[i][j] = pred(arr[i][j]);
      arr2[i][j] = pred2(arr2[i][j]);
    }
  }
};

input.forEach((instr) => {
  const m = instr.match(re);
  // console.log(m[1]);

  switch (m[1]) {
    case "turn on":
      operate(
        m[2],
        m[3],
        m[4],
        m[5],
        () => true,
        (x) => x + 1
      );
      break;
    case "turn off":
      operate(
        m[2],
        m[3],
        m[4],
        m[5],
        () => false,
        (x) => Math.max(0, x - 1)
      );
      break;
    case "toggle":
      operate(
        m[2],
        m[3],
        m[4],
        m[5],
        (x) => !x,
        (x) => x + 2
      );
      break;
  }
});

console.log(arr.reduce((acc, a) => acc + a.filter((x) => x).length, 0));
console.log(_.sum(arr2.map((a) => _.sum(a))));
