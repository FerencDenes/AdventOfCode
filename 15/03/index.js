const fs = require("fs");

const input = fs.readFileSync("03/input.txt").toString().trim();
const part1 = () => {
  let x = 0,
    y = 0;
  const visited = new Set();
  visited.add(`${x}, ${y}`);
  for (const ch of input) {
    switch (ch) {
      case "<":
        y--;
        break;
      case ">":
        y++;
        break;
      case "^":
        x--;
        break;
      case "v":
        x++;
        break;
      default:
        console.log(`Error ${ch}`);
    }
    visited.add(`${x}, ${y}`);
  }
  console.log(visited.size);
};
part1();

const part2 = () => {
  let x = [0, 0],
    y = [0, 0],
    i = 0;

  const visited = new Set();
  visited.add(`${x[0]}, ${y[0]}`);
  for (const ch of input) {
    i = (i + 1) % 2;
    switch (ch) {
      case "<":
        y[i]--;
        break;
      case ">":
        y[i]++;
        break;
      case "^":
        x[i]--;
        break;
      case "v":
        x[i]++;
        break;
      default:
        console.log(`Error ${ch}`);
    }
    visited.add(`${x[i]}, ${y[i]}`);
  }
  console.log(visited.size);
};

part2();
