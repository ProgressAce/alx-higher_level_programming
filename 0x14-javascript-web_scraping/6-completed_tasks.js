#!/usr/bin/node
/* Script that computes the number of tasks completed by user id.
 *
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only prints users with completed tasks */

// total users
// each user's total todos
// count users completed todo tasks
// add user to user_dict

const process = require('process');
const request = require('request');

if (process.argv.length !== 3) {
  console.log('USAGE: ./<program_name> api_url');
  process.exit();
}

const apiUrl = process.argv[2];

let count = 0; // count user-specific completed task
let prevCount = 0; // used to check if a user's task completion number should be updated
let prevUserId = 0; // used to check for next user's tasks(according to userId)

request(apiUrl, (error, response, body) => {
  if (error) { throw error; }

  const completedTasksDict = {};
  const todoList = JSON.parse(body);
  // todoLists = a list of dictionaries of tasks

  // The todo list of dictionaries are already sorted
  for (const task of todoList) {
    if (task.userId !== prevUserId) {
      count = 0;
      prevCount = 0;
      prevUserId = task.userId;
    }

    if (task.completed === true) {
      count += 1;
    }

    // update dict of completed tasks
    if (count > prevCount) {
      completedTasksDict[`${task.userId}`] = count;
    }
  }

  console.log(completedTasksDict);
});
