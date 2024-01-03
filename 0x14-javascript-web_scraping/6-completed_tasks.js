#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];

request(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    users_tasks = JSON.parse(body);

    all_tasks_done = {};
    for (task of users_tasks) {
      if (task.completed === true) {
	uid = task.userId.toString();
        if (uid in all_tasks_done) {
	  all_tasks_done.uid += 1;
	} else {
          all_tasks_done.uid = 1;
	}
      }
    }
    console.log(all_tasks_done);
  }
});
