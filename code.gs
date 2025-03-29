
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  const sheetName = 'today_nepse_data';
  
  let sheet = spreadsheet.getSheetByName(sheetName);
  
  if (!sheet) {
    sheet = spreadsheet.insertSheet(sheetName);
    Logger.log(`Sheet "${sheetName}" created.`);
  } else {
    Logger.log(`Sheet "${sheetName}" already exists.`);
  }


function getDataFromShareAPI() {
  const url = SHARE_API_ENDPOINT;

  console.log('getting data from url')
  const response = UrlFetchApp.fetch(url); 
  const json = response.getContentText();
  const data = JSON.parse(json); 

  sheet.clear(); 

  const headers = Object.keys(data);
  sheet.appendRow(headers);

  const numRows = data[headers[0]].length;

  const rows = [];

  for (let i = 0; i < numRows; i++) {
    const row = headers.map(header => data[header][i]); 
    rows.push(row);
  }

  sheet.getRange(2, 1, rows.length, headers.length).setValues(rows);
}
