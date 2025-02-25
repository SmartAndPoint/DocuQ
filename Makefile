.PHONY: check-npm
check-npm:
	@which npm > /dev/null || { echo 'npm is not installed. Check https://nodejs.org/en/download/package-manager for installation instructions' ; exit 1; }

.PHONY: init
init: check-npm
	npm install

.PHONY: build
build: init
	npm run build-prod

.PHONY: publish
publish: build
	npm publish --access public
