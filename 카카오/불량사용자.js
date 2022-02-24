function solution(user_id, banned_id) {
  function dfs(user, idx, str, table) {
    if (idx === user.length) {
      if (table[str]) {
        table[str].push(user);
      } else {
        table[str] = [user];
      }
      return;
    }
    dfs(user, idx + 1, str + user[idx], table);
    dfs(user, idx + 1, str + "*", table);
  }

  function getList(user, idx, list, answer) {
    if (list.length === banned_id.length) {
      if (!answer.includes(list.sort().join(""))) {
        answer.push(list.join(""));
      }
      return;
    }
    for (let i = 0; i < user[idx].length; i++) {
      if (!list.includes(user[idx][i])) {
        getList(user, idx + 1, [...list, user[idx][i]], answer);
      }
    }
  }

  let table = {};
  let bannedIdList = [];
  let answer = [];

  user_id.forEach((user) => dfs(user, 0, "", table));
  for (let bannedUser of banned_id) {
    bannedIdList.push(table[bannedUser]);
  }
  getList(bannedIdList, 0, [], answer);
  return answer.length;
}
