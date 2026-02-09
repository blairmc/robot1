#!/bin/bash

# Add all files to git
git add .

# Prompt for commit message
echo "Enter commit message:"
read commit_message

# Commit with the message
git commit -m "$commit_message"

# Push to git
git push origin main
