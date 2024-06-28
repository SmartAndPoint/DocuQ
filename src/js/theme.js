const lightTheme = {
    '--bg-color': '#ffffff',
    '--text-color': '#333333',
    '--input-bg': '#f0f0f0',
    '--input-text': '#333333',
    '--button-bg': '#007bff',
    '--button-text': '#ffffff',
    '--popup-shadow': '0 0 10px rgba(0,0,0,0.1)',
    '--close-button-color': '#666666',
};

const darkTheme = {
    '--bg-color': '#333333',
    '--text-color': '#f0f0f0',
    '--input-bg': '#555555',
    '--input-text': '#f0f0f0',
    '--button-bg': '#0056b3',
    '--button-text': '#ffffff',
    '--popup-shadow': '0 0 10px rgba(255,255,255,0.1)',
    '--close-button-color': '#aaaaaa',
};


function applyTheme(theme) {
    for (const [property, value] of Object.entries(theme)) {
        document.documentElement.style.setProperty(property, value);
    }
}

function setThemeBasedOnSystemPreference() {
    const isDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (isDarkMode) {
        applyTheme(darkTheme);
        import('../assets/atom-one-dark.css');
    } else {
        applyTheme(lightTheme);
        import('../assets/atom-one-light.css');
    }
}

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', setThemeBasedOnSystemPreference);

export { setThemeBasedOnSystemPreference };