# Makefile for Open Source Survey Results Jupyter Book

.PHONY: help install clean build serve test lint check-links validate

# Default target
help:
	@echo "Available commands:"
	@echo "  install      Install dependencies"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build the Jupyter Book"
	@echo "  serve        Serve the book locally"
	@echo "  test         Run all tests"
	@echo "  lint         Check markdown formatting (Python-based)"
	@echo "  check-links  Validate internal and external links"
	@echo "  validate     Validate configuration files"

# Install dependencies
install:
	pip install -r requirements-docs.txt

# Clean build artifacts
clean:
	jupyter-book clean docs/
	rm -rf docs/_build/

# Build the book
build: clean
	jupyter-book build docs/

# Serve the book locally
serve: build
	@echo "Opening book at http://localhost:8000"
	cd docs/_build/html && python -m http.server 8000

# Run comprehensive tests
test: validate lint build
	@echo "All tests passed!"

# Python-based markdown linting (instead of Node.js markdownlint)
lint:
	@echo "Checking markdown formatting..."
	python scripts/check_content.py

# Check internal and external links
check-links: build
	@echo "Checking internal links..."
	jupyter-book build docs/ --builder linkcheck

# Validate configuration files
validate:
	@echo "Validating _config.yml..."
	python -c "import yaml; yaml.safe_load(open('docs/_config.yml'))"
	@echo "Validating _toc.yml..."
	python -c "import yaml; yaml.safe_load(open('docs/_toc.yml'))"
	@echo "Configuration files are valid!"

# Quick development server with auto-reload (simplified version)
dev: build
	@echo "Starting development server..."
	@echo "Visit http://localhost:8000"
	@echo "Rebuild with 'make build' when you make changes"
	cd docs/_build/html && python -m http.server 8000

# Build for production (GitHub Pages)
production: clean
	jupyter-book build docs/ --builder html
	@echo "Production build complete in docs/_build/html/"

# Generate placeholder images (for testing)
generate-images:
	python scripts/generate_placeholder_images.py

# Check for broken internal references
check-refs:
	@echo "Checking for broken cross-references..."
	python scripts/check_references.py docs/

# Performance test (build time)
perf-test:
	@echo "Running performance test..."
	time make build

# Simple install without optional dependencies
install-minimal:
	pip install jupyter-book myst-parser matplotlib pillow