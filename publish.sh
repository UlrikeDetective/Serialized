#!/bin/sh
# Export your stories from the local database and push them to GitHub.
# GitHub then rebuilds the public site automatically (takes about a minute).
set -e
cd "$(dirname "$0")"

.venv/bin/python manage.py dumpdata stories --indent 2 --output stories/fixtures/stories.json
git add stories/fixtures/stories.json
git commit -m "Update stories" || echo "No changes to your stories."
git push
