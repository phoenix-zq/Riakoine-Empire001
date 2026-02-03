#!/bin/bash
# Navigate to the project folder
cd ~/Riakoine-Empire001

# Add all changes
git add .

# Commit with a timestamped message
git commit -m "auto-backup: $(date '+%Y-%m-%d %H:%M:%S')"

# Push to GitHub
git push origin main
