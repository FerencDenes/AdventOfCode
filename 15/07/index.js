const fs = require("fs");
const _ = require("lodash");

const input = fs.readFileSync("07/input.txt").toString().trim().split("\n");

const rules = new Map();
const re1 = RegExp("^(.*) -> (.*)$");

input.forEach((line) => {
  const m = line.match(re1);
  if (!m) {
    console.log(line);
  }
  rules.set(m[2], m[1]);
});

const NUM = RegExp("^(\\d+)$");
const NOT = RegExp("^NOT (.*)$");
const ASS = RegExp("^([a-z]+)$");
const OR = RegExp("^(.*) OR (.*)$");
const AND = RegExp("^(.*) AND (.*)$");
const RSHIFT = RegExp("^(.*) RSHIFT (.*)$");
const LSHIFT = RegExp("^(.*) LSHIFT (.*)$");
const wire = (k) => {
  const tryNum = k.match(NUM);
  if (tryNum) {
    return parseInt(tryNum[1]);
  }
  const rule = rules.get(k);

  try {
    if (typeof rule === "number") {
      return rule;
    }
    {
      const m = rule.match(ASS);
      if (m) {
        const res = wire(m[1]);
        rules.set(k, res);
        return res;
      }
    }
    {
      const m = rule.match(OR);
      if (m) {
        const res = wire(m[1]) | wire(m[2]);
        rules.set(k, res);
        return res;
      }
    }
    {
      const m = rule.match(AND);
      if (m) {
        const res = wire(m[1]) & wire(m[2]);
        rules.set(k, res);
        return res;
      }
    }
    {
      const m = rule.match(RSHIFT);
      if (m) {
        const res = wire(m[1]) >>> parseInt(m[2]);
        rules.set(k, res);
        return res;
      }
    }
    {
      const m = rule.match(LSHIFT);
      if (m) {
        const res = wire(m[1]) << parseInt(m[2]);
        rules.set(k, res);
        return res;
      }
    }
    {
      const m = rule.match(NUM);
      if (m) {
        const res = parseInt(m[1]);
        rules.set(k, res);
        return res;
      }
    }
    {
      const m = rule.match(NOT);
      if (m) {
        const res = ~wire(m[1]);
        rules.set(k, res);
        return res;
      }
    }
    console.err(`error ${k} ${rule} ${typeof rule}`);
  } catch (err) {
    console.log(k, typeof rule, rule, err);
  }
};

const a = wire("a");
console.log(a);

rules.clear();
input.forEach((line) => {
  const m = line.match(re1);
  if (!m) {
    console.log(line);
  }
  rules.set(m[2], m[1]);
});

rules.set("b", a);
console.log(wire("a"));
