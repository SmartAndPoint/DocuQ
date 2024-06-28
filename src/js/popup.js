import { searchDocuQ } from './search';

let currentPopup = null;

function showSearchPopup() {
    if (currentPopup) {
        document.body.removeChild(currentPopup);
    }

    const popup = document.createElement('div');
    popup.id = 'docuq-search-popup';
    popup.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: var(--bg-color);
        color: var(--text-color);
        padding: 20px;
        border-radius: 10px;
        box-shadow: var(--popup-shadow);
        z-index: 1000;
        width: 80%;
        max-width: 800px;
        max-height: 80vh;
        overflow-y: auto;
        font-family: Arial, sans-serif;
    `;

    const searchContainer = document.createElement('div');
    searchContainer.style.marginBottom = '20px';

    const input = document.createElement('input');
    input.type = 'text';
    input.placeholder = 'Enter your query...';
    input.style.cssText = `
        width: calc(100% - 110px);
        padding: 10px;
        font-size: 16px;
        border: 1px solid var(--input-text);
        border-radius: 5px;
        background-color: var(--input-bg);
        color: var(--input-text);
    `;
    
    const button = document.createElement('button');
    button.textContent = 'Search';
    button.style.cssText = `
        padding: 10px 20px;
        font-size: 16px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-left: 10px;
    `;
    button.onclick = () => searchDocuQ(input.value);

    const resultsContainer = document.createElement('div');
    resultsContainer.id = 'docuq-search-results-container';

    const resultsTitle = document.createElement('h2');
    resultsTitle.id = 'docuq-search-results-title';
    resultsTitle.style.cssText = `
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 18px;
        font-weight: bold;
    `;

    const results = document.createElement('div');
    results.id = 'docuq-search-results';
    results.classList.add('popup-content');
    results.style.cssText = `
        font-size: 16px;
        line-height: 1.6;
        color: var(--text-color);
    `;

    const closeButton = document.createElement('button');
    closeButton.textContent = 'x';
    closeButton.style.cssText = `
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 24px;
        background: none;
        border: none;
        cursor: pointer;
        color: var(--close-button-color);
    `;
    closeButton.onclick = () => hidePopup();

    searchContainer.appendChild(input);
    searchContainer.appendChild(button);

    resultsContainer.appendChild(resultsTitle);
    resultsContainer.appendChild(results);

    popup.appendChild(closeButton);
    popup.appendChild(searchContainer);
    popup.appendChild(resultsContainer);

    document.body.appendChild(popup);
    currentPopup = popup;

    input.focus();

    input.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            const query = input.value;
            searchDocuQ(query);
        }
    });

};

function hidePopup() {
    if (currentPopup) {
        document.body.removeChild(currentPopup);
        currentPopup = null;
    }
}

export { showSearchPopup, hidePopup };