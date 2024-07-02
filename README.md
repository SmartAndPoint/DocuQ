# DocuQ

DocuQ is a OpenSource chat that redefines the way users interact with your site documentation. By transforming your project documentation into an interactive and user-friendly knowledge base, DocuQ empowers users to quickly find the information they need and write their code efficiently.

## Why Choose DocuQ?

- Unparalleled User Experience: DocuQ’s sleek and intuitive interface makes navigating your documentation a breeze, enhancing user engagement and satisfaction.
- Instant Code Snippets: Users can generate and copy code snippets directly from your documentation, reducing development time and increasing productivity.
- Dynamic Search Capabilities: With an intelligent search popup, DocuQ allows users to find relevant information in seconds, minimizing frustration and maximizing efficiency.
- Customizable and Flexible: Easily tailor the appearance and functionality of DocuQ to align with your brand and meet your specific needs.

Transform Your Documentation Today!

DocuQ is designed for seamless integration into both open-source and proprietary projects. By leveraging powerful features like syntax highlighting and persistent query history, DocuQ ensures your documentation is not just read, but actively used and appreciated.

## Features

🌟 Interactive Search Popup

DocuQ provides a sleek, interactive search popup that allows users to quickly find the information they need within your documentation. No more endless scrolling—just type and find!

🎨 Beautiful Syntax Highlighting

With highlight.js at its core, DocuQ delivers beautiful, customizable syntax highlighting. Whether you’re in light or dark mode, your code will always look its best.

🗂️ Persistent Query History

DocuQ remembers your users’ queries and responses, making it easier to revisit previous searches. This history is maintained even if the popup is closed, ensuring a smooth user experience.

🔐 Secure and Flexible Integration

DocuQ supports integration with both open-source and proprietary projects. It uses secure server-side handling for sensitive operations, ensuring your API keys and data remain safe.

💼 Easy Customization

Customize the look and feel of DocuQ to match your brand. With custom CSS support, you can tweak every aspect of the search popup and syntax highlighting to fit your needs.

## Installation

### Via NPM Package

```bash
npm install docuq
```

### Via CDN

```html
<script src="https://cdn.jsdelivr.net/gh/SmartAndPoint/DocuQ/dist/docuq.js"></script>
<script>
    window.addEventListener('load', function() {
    const docuqUrl = 'http://api.docuq.io/search';
    window.initializeDocuQ(docuqUrl);
    })
</script>

```

## Usage

```javascript
// In your project's entry file
import { initializeDocuQ } from 'docuq';
const docuqUrl = 'http://api.docuq.io/search';
document.addEventListener('DOMContentLoaded', initializeDocuQ(docuqUrl));
```

## Roadmap

## License
![GitHub](https://img.shields.io/github/license/SmartAndPoint/DocuQ)
