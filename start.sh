#!/bin/bash
pip install python-multipart
uvicorn main:app --host 0.0.0.0 --port 10000
uvicorn main:app --host=0.0.0.0 --port=10000
