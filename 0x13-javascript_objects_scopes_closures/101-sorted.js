#!/usr/bin/node
const dict = require('./101-data.js').dict;
const group_by_user_id = {};
Object.keys(dict).forEach(value => {
	const user_id = dict[value];
	if (!group_by_user_id[user_id]) {
		group_by_user_id[user_id] = [];
	}
	group_by_user_id[user_id].push(value);
});
console.log(group_by_user_id);
