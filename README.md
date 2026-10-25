# Serialized

A Django application for publishing episodic fiction.

- **Live site:** https://ulrikedetective.github.io/Serialized/
- **Repository:** https://github.com/UlrikeDetective/Serialized

👉 **New here? Read [start.md](start.md) for step-by-step setup and usage instructions.**

## Key Features
- **Organized Hierarchy**: Manage data through Story and Chapter relationships.
- **Scheduled Publishing**: Chapters remain hidden until their designated `publish_date`.
- **E-Reader Experience**: Optimized reading view with drop caps, readable line widths, and intuitive navigation cards.
- **Modern Hacker Aesthetic**: Minimalist monospace design with high-contrast black/white and bright yellow highlights.
- **Free Static Hosting**: No server to maintain. The public site is plain HTML on GitHub Pages.
- **SEO Friendly**: Uses slugs and clean URL patterns.

## How It Works

```
 Your computer                         GitHub
┌──────────────────────┐   publish   ┌──────────────────────────────┐
│ Django + admin       │ ──────────▶ │ GitHub Actions builds the    │
│ (write & preview)    │  git push   │ site with django-distill     │
│ db.sqlite3           │             │            │                 │
└──────────────────────┘             │            ▼                 │
                                     │ GitHub Pages (public site)   │
                                     └──────────────────────────────┘
```

1. You write stories in the Django admin on your own computer.
2. `./publish.sh` exports them to `stories/fixtures/stories.json` and pushes to GitHub.
3. GitHub Actions (`.github/workflows/deploy.yml`) loads that file, renders every page to HTML with [django-distill](https://github.com/meeb/django-distill), and deploys it to GitHub Pages.
4. The site is also rebuilt every day at 06:00 UTC, so scheduled chapters appear on their own.

## Quick Reference

| Task | Command |
|------|---------|
| Start local server | `.venv/bin/python manage.py runserver` |
| Admin | http://localhost:8000/admin/ |
| Publish stories | `./publish.sh` |

## Project Structure

```
stories/
├── models.py                  # Story and Chapter
├── views.py                   # Page logic
├── urls.py                    # URLs + which pages to export
├── settings.py
├── fixtures/stories.json      # Published stories (created by publish.sh)
├── static/stories/style.css   # All styling
└── templates/                 # HTML layouts
.github/workflows/deploy.yml   # Builds and deploys the website
publish.sh                     # Export + push in one step
start.md                       # Step-by-step guide
```

## Tech Stack
- Django 6.0
- django-distill (static export)
- SQLite
- GitHub Pages + GitHub Actions
- Custom CSS (Modern Hacker / Minimalist)
