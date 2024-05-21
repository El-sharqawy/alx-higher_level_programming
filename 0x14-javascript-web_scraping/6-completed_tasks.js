#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const tasksDone = {};
    const tasks = JSON.parse(body);

    for (const num in tasks) {
      const task = tasks[num];
      if (task.completed === true) {
        if (tasksDone[task.userId] === undefined) {
          tasksDone[task.userId] = 1;
        } else {
          tasksDone[task.userId]++;
        }
      }
    }
    console.log(tasksDone);
  } else {
    console.log('An error occured. Status code: ' + res.statusCode);
  }
});
