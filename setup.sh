#!/bin/bash

PROJECT=street-parking-reservation

export FLASK_ENV=development
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/$PROJECT
export JWT_SECRET_KEY=hhgaghhgsdhdhdd
python run.py