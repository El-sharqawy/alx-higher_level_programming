#!/usr/bin/node

function getFact (a) {
  if (a === 1 || !a || isNaN(a))
    return (1);
  return (a * getFact(a - 1));
}

console.log(getFact(parseInt(process.argv[2])));

