#!/bin/sh

# Any other initialization or setup commands can go here

# Start Uvicorn with live reload for development
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
