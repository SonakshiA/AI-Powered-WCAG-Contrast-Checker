# AI-Powered WCAG Contrast Checker

The Web Content Accessibility Guidelines (WCAG) provide recommendations for creating accessible digital content. For AA level compliance regarding color contrast, the following guidelines apply:

## Text and Background Contrast (AA Level)
Normal Text: The contrast ratio between text and background must be at least 4.5:1.
Large Text: For text larger than 18pt (24px) or 14pt (18.66px) if bold, the contrast ratio must be at least 3:1.

## Non-Text Elements (UI Components and Graphical Objects)
Non-text elements, such as icons, buttons, and graphical components, must have a contrast ratio of at least 3:1 against their adjacent background.

## About the Project

This project inputs the hex codes for the background and foreground colors and checks for the three criteria listed above. The goal is to improve digital accessibility!

Furthermore, an AI-powered model (Qwen/QwQ-32B-Preview) sourced from HuggingFace gives foreground color recommendations to improve readability and pass the WCAG criteria.