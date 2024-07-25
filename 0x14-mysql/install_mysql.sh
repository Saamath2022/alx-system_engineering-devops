#!/usr/bin/env bash
# Install MySQL 5.7.x on the server

sudo apt-get update
sudo apt-get install -y mysql-server-5.7

# Verify installation
mysql --version
