#!/usr/bin/node

const axios = require('axios');

const url = process.argv[2];

axios.get(url)
  .then(response => {
    if (response.status === 200) {
      const completed = {};
      const tasks = response.data;
      
      tasks.forEach(task => {
        if (task.completed === true) {
          completed[task.userId] = (completed[task.userId] || 0) + 1;
        }
      });

      console.log(completed);
    } else {
      console.log('An error occurred. Status code: ' + response.status);
    }
  })
  .catch(error => {
    console.log(error.message);
  });
