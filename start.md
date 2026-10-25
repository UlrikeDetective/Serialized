# Getting Started with Serialized

This guide walks you through everything step by step: setting the project up,
writing stories, and publishing them to your website on GitHub Pages.

**How it works in one sentence:** Django runs only on your own computer, where you
write in the admin. When you publish, GitHub turns the site into plain HTML pages
and puts them online at https://ulrikedetective.github.io/Serialized/.

All commands are typed in the Terminal, inside the project folder:

```sh
cd ~/projects/Django/Django_Serialized
```

---

## Part 1: One-time setup on your computer

You only need to do this once (or again on a new computer).

### Step 1: Create the virtual environment

The virtual environment is a private folder (`.venv`) that holds Django and the
other packages for this project.

```sh
python3 -m venv .venv
```

### Step 2: Install the packages

```sh
.venv/bin/pip install -r requirements.txt
```

### Step 3: Prepare the database

```sh
.venv/bin/python manage.py migrate
```

> **Only on a new computer** (where there is no `db.sqlite3` file yet): load the
> stories that are already published, and create an admin login:
>
> ```sh
> .venv/bin/python manage.py loaddata stories
> .venv/bin/python manage.py createsuperuser
> ```

### Step 4: Check that it works

```sh
.venv/bin/python manage.py runserver
```

Open http://localhost:8000/ in your browser. You should see the site with its
black/white/yellow styling. Press `Ctrl + C` in the Terminal to stop the server.

---

## Part 2: One-time setup on GitHub

### Step 5: Make sure the repository is public

GitHub Pages is free only for public repositories.
Open https://github.com/UlrikeDetective/Serialized/settings and check under
**Danger Zone → Change repository visibility** that it says *public*.

### Step 6: Turn on GitHub Pages

1. Open https://github.com/UlrikeDetective/Serialized/settings/pages
2. Under **Build and deployment → Source**, choose **GitHub Actions**.

That's it. There is nothing else to configure.

### Step 7: Push the project

```sh
git push
```

Then open the **Actions** tab of the repository
(https://github.com/UlrikeDetective/Serialized/actions). You'll see a run called
**Build and deploy site**. When it shows a green tick (about a minute), your site
is live at https://ulrikedetective.github.io/Serialized/.

---

## Part 3: Everyday use

### Writing a story or chapter

1. Start the server:

   ```sh
   .venv/bin/python manage.py runserver
   ```

2. Open http://localhost:8000/admin/ and log in.
3. Add or edit a **Story** or **Chapter**.
4. Preview it at http://localhost:8000/.
5. Stop the server with `Ctrl + C` when you're done.

### Publishing

```sh
./publish.sh
```

This saves your stories to `stories/fixtures/stories.json`, commits that file and
pushes it to GitHub. About a minute later the website is updated.

### Scheduling a chapter for later

Set the chapter's **Publish date** in the admin to a date in the future, then run
`./publish.sh` as usual. The chapter stays hidden on the website until that date.

GitHub rebuilds the site **every day at 06:00 UTC** (07:00 in German winter time,
08:00 in summer time). So a scheduled chapter appears on the first daily rebuild
after its publish date.

> Note: the times you enter in the admin are in **UTC**, not German time.

To publish a scheduled chapter right away without waiting, open the **Actions**
tab, click **Build and deploy site**, then **Run workflow**.

### Changing the design or templates

- Styling: `stories/static/stories/style.css`
- Page layouts: `stories/templates/`

Check your changes at http://localhost:8000/, then publish them like any other
code change:

```sh
git add .
git commit -m "Describe your change"
git push
```

---

## Troubleshooting

**The site on localhost has no styling.**
Make sure `.env` doesn't contain `DEBUG=False`. The local server only serves the
CSS when debug mode is on, and it is on by default.

**`.venv/bin/python: No such file or directory`**
You're either in the wrong folder (see the `cd` command at the top) or haven't
done Step 1 yet.

**I forgot my admin password.**

```sh
.venv/bin/python manage.py changepassword
```

**The website didn't update after publishing.**
Open the **Actions** tab. A red cross means the build failed. Click on it to see
the error message. A grey run that's still spinning just needs another minute.

**`./publish.sh` says "No changes to your stories."**
Nothing in the admin changed since the last publish, so there was nothing to
upload. Design changes have to be committed and pushed with git (see above).

**I want to see exactly what will go online before publishing.**
Run the same build GitHub does, then open the pages in your browser:

```sh
DEBUG=False SITE_PREFIX=Serialized/ .venv/bin/python manage.py distill generate --collectstatic --force --output-directory site
python3 -m http.server 8765 -d site
```

Then open http://localhost:8765/Serialized/ and stop with `Ctrl + C` when done.
(The `site/` folder is not uploaded to GitHub.)
