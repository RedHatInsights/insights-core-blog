#!/usr/bin/env bash
###################

# This script runs pelican and ghp-import commands to generate the content in the output directory then push the
# generated content to the gh-pages branch in the github repo.

# Build the web content from markup
pelican content -o output -s pelicanconf.py

# Commit and push the content in the output directory to the gh-pages branch
ghp-import -p output
