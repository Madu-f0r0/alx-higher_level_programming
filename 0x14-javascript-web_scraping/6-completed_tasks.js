#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];

request(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    usersTasks = JSON.parse(body);

    allTasksDone = {};
    for (task of usersTasks) {
      if (task.completed === true) {
        uid = task.userId.toString();
        if (uid in allTasksDone) {
	  allTasksDone.uid += 1;
        } else {
          allTasksDone.uid = 1;
        }
      }
    }
    console.log(allTasksDone);
  }
});
