import DOMPurify from 'dompurify';
import { marked } from 'marked';
import { initializeHighlighting } from './utils';

let currentResults = '';

function getPageContent() {
    const content = document.body ? document.body.innerText : '';
    return content.replace(/\s+/g, ' ').trim();
}

async function searchDocuQ(query, docuqUrl) {
    if (query instanceof Event) {
        return;
    }

    query = String(query).trim();

    if (!query) return;

    try {
        console.log("Initiating search with query:", query);
        const pageContent = getPageContent();
        console.log("DocuQ URL:", docuqUrl);
        const response = await fetch(docuqUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Origin': window.location.origin
            },
            body: JSON.stringify({ query: query, content: pageContent }),
        });

        console.log("Received response:", response);
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        const resultsDiv = document.getElementById('docuq-search-results');
        const resultsTitleDiv = document.getElementById('docuq-search-results-title');
        const inputField = document.querySelector('#docuq-search-popup input[type="text"]');
        resultsDiv.innerHTML = '';
        currentResults = '';

        resultsTitleDiv.textContent = `Results for: "${query}"`;
        resultsTitleDiv.style.display = 'block';

        while (true) {
            const { value, done } = await reader.read();
            if (done) break;
            const decodedValue = decoder.decode(value);
            console.log("Appending decoded value:", decodedValue);
            currentResults += decodedValue;
            resultsDiv.innerHTML = DOMPurify.sanitize(marked.parse(currentResults));
            initializeHighlighting();

        }
        inputField.value = '';
    } catch (error) {
        console.error('Error:', error);
        const resultsTitle = document.getElementById('docuq-search-results-title');
        const results = document.getElementById('docuq-search-results');
        resultsTitle.textContent = 'Error';
        results.textContent = 'An error occurred while processing your request. Please try again.';
    }
    return `Response for query: ${query}`;
}

export { searchDocuQ };
