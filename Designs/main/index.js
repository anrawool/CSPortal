function getFormattedDate() {
    const today = new Date();
    const day = today.getDate();
    const month = today.getMonth() + 1;
    const formattedDate = `${day < 10 ? '0' : ''}${day}/${month < 10 ? '0' : ''}${month}`;
    return formattedDate;
}

// Get the div element where you want to display the date.
const dateDisplayDiv = document.getElementById('dat');

// Set the innerHTML of the div to the formatted dat
dateDisplayDiv.innerHTML = getFormattedDate();
