import '../assets/styles.css';
import {setThemeBasedOnSystemPreference} from './theme';
import {showSearchPopup, hidePopup} from './popup';

document.addEventListener('DOMContentLoaded', () => {
    setThemeBasedOnSystemPreference();
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', setThemeBasedOnSystemPreference);

    const searchButton = document.createElement('button');
    searchButton.textContent = 'DocuQ Search';
    searchButton.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        padding: 10px 20px;
        font-size: 16px;
        background-color: var(--button-bg);
        color: var(--button-text);
        border: none;
        border-radius: 5px;
        cursor: pointer;
        z-index: 1000;
    `;
    searchButton.onclick = showSearchPopup;
    document.body.appendChild(searchButton);

    document.addEventListener('keydown', (event) => {
        if (event.metaKey && event.key === '7') {
            event.preventDefault();
            showSearchPopup();
        } else if (event.key === 'Escape') {
            hidePopup();
        }
    });
});