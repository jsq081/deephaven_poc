# Deephaven Streaming Poc

This project utilizes Deephaven for real-time data processing and analysis. This README will guide you through the installation and running of the Deephaven server.

## Prerequisites

- Python 3.7 or higher
- Pip

## Installation

To install the Deephaven Python client, run the following command:

```bash
pip install deephaven
```

## Running the Deephaven Server
```bash
deephaven server --jvm-args "-Xmx4g -Dauthentication.psk=YOUR_PASSWORD"
```

## Usage
Once the server is running, you can access the Deephaven UI in your web browser at http://localhost:10000.