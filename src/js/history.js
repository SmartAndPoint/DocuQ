// Function to get history from sessionStorage
function getHistory() {
    const history = sessionStorage.getItem('queryHistory');
    return history ? JSON.parse(history) : [];
}

// Function to save history to sessionStorage
function saveHistory(history) {
    sessionStorage.setItem('queryHistory', JSON.stringify(history));
}

// Function to add a query and response to the history
function addToHistory(query, response) {
    const history = getHistory();
    history.push({ query, response });
    saveHistory(history);
}

// Function to clear the history
function clearHistory() {
    sessionStorage.removeItem('queryHistory');
}

export { getHistory, saveHistory, addToHistory, clearHistory };