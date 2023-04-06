// get elements
const form = document.querySelector('form');
const tableBody = document.querySelector('tbody');
const exportBtn = document.querySelector('#export-btn');

// add submit event listener to form
form.addEventListener('submit', (e) => {
  e.preventDefault();

  // get form data
  const formData = new FormData(form);
  const name = formData.get('name');
  const id = formData.get('id');

  // add data to table
  const newRow = document.createElement('tr');
  newRow.innerHTML = `
    <td>${name}</td>
    <td>${id}</td>
  `;
  tableBody.appendChild(newRow);

  // reset form
  form.reset();
});

// add click event listener to export button
exportBtn.addEventListener('click', () => {
  // create CSV data
  let csvData = 'data:text/csv;charset=utf-8,Name,ID\n';
  tableBody.querySelectorAll('tr').forEach((row) => {
    const cells = row.querySelectorAll('td');
    const name = cells[0].innerText;
    const id = cells[1].innerText;
    csvData += `${name},${id}\n`;
  });

  // create download link and click it
  const encodedData = encodeURI(csvData);
  const link = document.createElement('a');
  link.setAttribute('href', encodedData);
  link.setAttribute('download', 'attendance.csv');
  document.body.appendChild(link);
  link.click();
});
