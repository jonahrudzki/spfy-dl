---

# spfy-dl

A lightweight Spotify downloader built with Node.js that allows you to download tracks, albums, and playlists using Spotify links.
Note - Changes to google/ytmusic api Oauth may render this project outdated as of 14/04/2026

> This tool does not download audio directly from Spotify. It retrieves metadata from Spotify and sources audio from external providers.

---

## Features

* Download individual tracks, albums, or playlists
* Simple command-line interface
* Automatic track matching from external sources
* Configurable output directory
* Metadata tagging support (if implemented)

---

## Getting Started

### Prerequisites

* Node.js (v16 or later recommended)
* npm or yarn
* FFmpeg installed and available in your system PATH

---

### Installation

Clone the repository:

```bash
git clone https://github.com/jonahrudzki/spfy-dl.git
cd spfy-dl
```

Install dependencies:

```bash
npm install
```

---

## Usage

Basic usage:

```bash
node index.js <spotify-link>
```

Example:

```bash
node index.js https://open.spotify.com/track/...
```

---

## Options

| Flag            | Description             |
| --------------- | ----------------------- |
| `-o, --output`  | Set output directory    |
| `-q, --quality` | Set audio quality       |
| `--playlist`    | Force playlist download |
| `--album`       | Force album download    |

Adjust these options based on your implementation.

---

## Project Structure

```
spfy-dl/
├── src/
├── index.js
├── package.json
└── README.md
```

---

## How It Works

1. Extracts metadata from a Spotify URL
2. Searches for corresponding audio from external sources
3. Downloads and processes audio using FFmpeg
4. Saves files locally with structured naming

---

## Disclaimer

This project is for educational purposes only.

* Do not use this tool to download copyrighted material without permission
* Ensure compliance with Spotify’s Terms of Service
* The author is not responsible for misuse

---

## Roadmap

* Improve matching accuracy
* Add graphical interface (e.g. Electron)
* Batch download support
* Enhanced metadata tagging
* Cross-platform builds

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## License

MIT License

---

## Author

Jonah Rudzki
[https://github.com/jonahrudzki](https://github.com/jonahrudzki)

---
