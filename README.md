# Logger Package

A simple Python logger package that allows you to log messages to a text file with a custom heading and timestamp.

## Usage

```
from logger import Logger

# Initialize logger with log file name and heading
log = Logger("log Name", "function name")

# Write a log message
log.Write("this is log")
```

## Features
- Logs are stored in the `Logs` folder in the project directory.
- Each log file is named as specified during initialization.
- The first line of each log Writtem contains the timestamp and heading.
- Each call to `Write` appends a new line to the log file.