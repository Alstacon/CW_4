#!/bin/bash
python3 create_tables.py
python3 load_fixtures.py
exec "$@"