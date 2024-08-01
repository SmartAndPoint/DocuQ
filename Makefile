# UI

.PHONY: ui-init
ui-init:
	cd DocuQ-UI && npm install

.PHONY: ui-build
ui-build: ui-init
	cd DocuQ-UI && npm run build-prod

.PHONY: ui-publish
ui-publish: ui-build
	cd DocuQ-UI && npm publish --access public


# Backend

.PHONY: backend-build
backend-build:
	cd DocuQ-Backend && docker build -t docuq-server .

