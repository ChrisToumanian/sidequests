#!/bin/bash
DB_NAME="sidequests"
DB_USER="dm"
DB_PASS="password"  # Use a secure password in production environment

command -v psql > /dev/null || { echo >&2 "psql command not found. Please install PostgreSQL."; exit 1; }

echo "Creating database..."
sudo -u postgres psql -c "CREATE DATABASE $DB_NAME;"

echo "Creating user..."
sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';"

echo "Creating tables on database..."
sudo -u postgres psql -d $DB_NAME -f setup.sql

# log in as user with: psql -U dm -d sidequests -h localhost
echo "Granting privileges to user on database..."
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
sudo -u postgres psql -d $DB_NAME -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA PUBLIC TO $DB_USER;"

echo "Done."
