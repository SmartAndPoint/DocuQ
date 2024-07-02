import hljs from 'highlight.js/lib/common';

function initializeHighlighting() {
    document.querySelectorAll('.popup-content pre code').forEach((block) => {
        hljs.highlightElement(block);
    });
}

export { initializeHighlighting };