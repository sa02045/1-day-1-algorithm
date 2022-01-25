function solution(id_list, report, k) {
  let stoppedIdTable = {};
  let reportingTable = {};

  id_list.forEach((id) => {
    stoppedIdTable[id] = 0;
    reportingTable[id] = [];
  });

  for (const info of report) {
    const [reporter, reportee] = info.split(" ");
    if (!reportingTable[reporter].includes(reportee)) {
      stoppedIdTable[reportee]++;
      reportingTable[reporter].push(reportee);
    }
  }

  const stoppedId = Object.entries(stoppedIdTable)
    .filter((user) => user[1] >= k)
    .map((user) => user[0]);

  return Object.values(reportingTable).map(
    (reportingId) => reportingId.filter((id) => stoppedId.includes(id)).length
  );
}
