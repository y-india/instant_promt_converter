# Prompt Refinement Chrome Extension (Practice Version)

This repository contains a **practice implementation** of a Chrome extension + local backend system designed to improve raw text prompts using an LLM.

> Note: This is a simplified/public version created for learning and demonstration.
> The full production version of this project is maintained in a private repository.

---

## Overview

This tool focuses on a simple but effective workflow:

1. Select text in the browser
2. Copy it manually
3. Trigger the extension
4. Send text to a local backend
5. Receive an improved, structured version

The goal is to **reduce friction in prompt writing** while keeping the system reliable and easy to use.

---

## Architecture

### 1. Chrome Extension (Frontend)

* Trigger-based interaction (no auto-capture)
* Sends copied text to backend
* Displays processed output
* Includes replace functionality

### 2. FastAPI Backend

* Handles `/process` endpoint
* Sends text to LLM for refinement
* Returns improved version
* Runs locally for better control and security

### 3. Communication

* HTTP-based (POST requests)
* JSON data exchange
* CORS enabled for local development

---

## Key Design Decisions

### Manual Copy Over Automation

Instead of automatic clipboard capture, this project uses manual copy (Ctrl+C).
This avoids permission issues and improves cross-app reliability.

### Local Backend

* Keeps API keys secure
* Enables custom logic and debugging
* Makes the system extensible

### Simplicity First

The system avoids unnecessary complexity and focuses on:

* Stability
* Speed
* Practical usability

---

## Features

* Capture selected text (manual copy)
* Send text to backend
* Improve prompt using LLM
* Display processed result
* Replace original text
* Basic save/reuse functionality

---

## Limitations

* Requires manual copy
* No automatic context awareness
* Limited storage system
* No cloud sync

These trade-offs are intentional for this practice version.

---

## Purpose of This Repository

This project was built to:

* Practice building Chrome extensions
* Work with FastAPI backend services
* Understand LLM integration workflows
* Explore real-world productivity tooling design

---

## Future Improvements (Planned Ideas)

* Prompt history with search
* Predefined transformation templates
* Keyboard shortcut triggers
* Inline DOM-based replacement
* Multiple processing modes (summarize, expand, rephrase)

---

## Disclaimer

This repository represents a **learning and experimentation version** of the project.

The complete and more advanced implementation is kept private.

---

## Summary

A minimal, reliable system for improving prompts using a Chrome extension and a local FastAPI backend.
