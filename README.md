# My Engineering Portfolio

This is my portfolio site for our intro-to-engineering/robotics course. It's
a plain HTML/CSS website — no build tools, nothing to install — that
documents each in-class activity and project as I complete it, and doubles
as a public page I can point people to.

If you're reading this in **Dr. E's template repository**, this isn't your
portfolio yet — it's the starting point. Follow **Setup**, below, to turn it
into your own live, personalized site.

## Setup: from template to live portfolio

Do these steps once, in order, the first time you get this template. Each one
builds on the last, so don't skip ahead.

### 1. Create a GitHub account (skip if you already have one)

Go to [github.com/join](https://github.com/join) and sign up with your email.
Use a professional-looking username — future employers and classmates will
see it in your portfolio's web address.

### 2. Use the template to create your own repository

On **Dr. E's template repository page**, click the green **"Use this
template"** button in the top right.

You'll see two options. Pick **"Create a new repository"** — not "Open in a
codespace." ("Open in a codespace" starts an unsaved workspace that isn't
actually attached to a repository in your account yet, which is an easy way
to lose track of your work. "Create a new repository" makes the real thing in
your account first, cleanly.)

On the page that follows:

- [ ] **Owner:** make sure it's your own account, not Dr. E's.
- [ ] **Repository name:** give it a real name now, something like
      `en1-portfolio` or `robotics-portfolio`. Avoid the word "template."
      Also avoid naming it generically `portfolio` because this is just for this class; you'll likely want a generic name later for a bigger portfolio
      that combines all your work from multiple classes. This repo should be its
      own separate project.
- [ ] **Visibility:** leave it set to **Public**. GitHub Pages (the free
      publishing tool we're using) requires a public repository on a free
      account, and a portfolio is meant to be public anyway.
- [ ] Click **Create repository**.

You now have your own copy of this template, under your own account.

### 3. Turn on GitHub Pages

Do this now, before you start editing, so the one-time infrastructure setup
is out of the way and you can watch your own changes go live as you make
them later.

1. On GitHub.com, open **your repository** and go to **Settings → Pages**.
2. Under "Build and deployment," set **Source** to **"Deploy from a
   branch,"** branch **`main`**, folder **`/ (root)`**. Click **Save**.
3. Wait about a minute, then refresh the page. GitHub will show you your
   live URL — it looks like:

   ```
   https://<your-github-username>.github.io/<your-repo-name>/
   ```

No build step is needed — the site is plain HTML/CSS, and the `.nojekyll`
file tells GitHub Pages to serve it as-is.

### 4. Confirm your site is live

Visit the URL from step 3. Right now it'll still show the template's
placeholder content — `FIRSTNAME LASTNAME`, a generic hero image, and so on.
That's expected. The point of this step is just to confirm the plumbing
works: the page loads, images show up, and the activity/project cards link
to their pages. You'll open your editor and personalize the actual content
next.

### 5. Open your new repository in a Codespace

A Codespace is a full code editor (VS Code) plus a computer to run it on,
both running in your browser — nothing to install.

From **your new repository** (not the template!):

1. Click the green **"Code"** button.
2. Select the **"Codespaces"** tab.
3. Click **"Create codespace on main."**

The first time will take a minute or two while it sets everything up.
Once it's ready, `index.html` opens automatically, and a **"Portfolio
Preview"** tab should pop up showing your site running live — that preview
auto-refreshes as you edit and save files. If GitHub Copilot Chat isn't
already visible, look for its icon in the left sidebar; that's your AI
assistant for the next step.

### 6. Personalize your content with your AI assistant

Now make it yours. Don't scroll through the HTML hunting for placeholder
text by hand — ask your AI assistant (GitHub Copilot Chat, in the Codespace's
left sidebar) to make the changes for you. For example:

> Replace every "FIRSTNAME LASTNAME" placeholder in this site with my name,
> "Jane Smith." Update the LinkedIn and GitHub links in index.html's social
> box to my profiles: <your LinkedIn URL> and <your GitHub URL>.

Things to personalize:

- [ ] Your name, replacing `FIRSTNAME LASTNAME` everywhere it appears.
- [ ] Your own header/banner image, replacing `images/header.jpg`.
- [ ] Your LinkedIn and GitHub links in `index.html`'s social box.
- [ ] Confirm you have the rights to publish any images you use — swap out
      any placeholder/stock images that aren't yours.

Then, as you complete each activity/project, ask your assistant to replace
its lorem-ipsum text and placeholder image, and give its `<title>` tag a
real, specific value (see [AGENTS.md](./AGENTS.md)).

**Good habits working with an AI assistant:**

- Be specific about *what* you want and *where* (which page, which section).
- After it makes a change, open the preview and actually look — don't just
  trust that it worked.
- Read the diff before accepting it. If something looks unfamiliar, ask the
  assistant to explain it.
- Never let it invent your results, reflections, or data — that content has
  to be yours.

### 7. Save your work: commit and sync

Editing a file in the Codespace only changes it on the temporary computer
running your Codespace. That's not the same as saving to GitHub, and it does
**not** update your live site. To make a change permanent and get it onto
your live site, you do two things: **commit**, then **sync**.

- **Commit** = save a labeled checkpoint of your changes into the project's
  history. Think of it like a save file in a video game — you can always
  come back to it later.
- **Sync** (also called "push") = upload that checkpoint from your Codespace
  up to GitHub.com. This is the step that actually updates your live site,
  since GitHub Pages republishes from what's on GitHub, not from what's
  sitting unsaved in your Codespace.

**Why bother with a message when you commit?** That short message is a
label for the checkpoint — it's what lets you (or anyone looking at your
project's history later) understand what changed and why, without having to
reread every line of code. Compare `"Personalize name and social links"` to
just `"changes"` — the first tells a story, the second tells you nothing.
Keep it short and specific: what did you just do?

**How often should you commit?** Whenever you finish a meaningful chunk of
work — for example, after personalizing your name and links, after
finishing a project page's writeup, or after adding a photo gallery. You
don't need to commit after every tiny edit, but don't wait until the very
end of an assignment to do it once, either. A good rule of thumb: commit
whenever you'd be annoyed to lose the work if your browser crashed right
now.

To actually do it, in the Codespace:

1. Open the **Source Control** icon in the left sidebar (it looks like a
   branching path, and shows a number badge for how many files you've
   changed).
2. Click a changed file to review what it changed — added lines show in
   green, removed lines in red. Make sure the change looks like what you
   intended.
3. Type your short commit message in the box at the top.
4. Click the checkmark (✓) button to **commit**.
5. Click **Sync Changes** to **push** your commit(s) up to GitHub.

Nothing you do in a Codespace is backed up to GitHub, or visible on your
live site, until you've done both steps — commit *and* sync.

Refresh your live URL to check your change. GitHub Pages usually updates
within a minute of a sync, but it can occasionally take a couple of minutes
— if you don't see your change right away, wait a bit and try a hard
refresh (or an incognito/private window, in case your browser cached the
old page) before assuming something's wrong.

Once your name, links, and images are your own and synced, that live link
is your public portfolio — this is what you send to classmates, an
instructor, or a recruiter.

## Viewing it while you work

- **In a Codespace:** the "Portfolio Preview" tab (port 5500) shows your
  site live and refreshes as you save changes. If it doesn't pop up
  automatically, open the **Ports** tab at the bottom of VS Code and click
  the globe icon next to port 5500.
- **Locally, outside a Codespace:** just open `index.html` in a browser
  (double-click it, or in VS Code right-click it and choose "Open with Live
  Server" if you have that extension installed).
- **Live, on the internet:** your GitHub Pages URL from Setup, step 3 —
  this is what everyone else sees.

## How the site is organized

```
index.html          Home page — intro + a grid of cards, one per activity/project
index.css           Styles just for the home page
project.css         Shared styles for every activity/project detail page
theme.css           Colors/fonts used by both stylesheets, in one place
template.html       Starting point for a new activity or project page
activityNN.html     One in-class activity's page (e.g. activity01.html)
projectNN.html      One project's page (e.g. project01.html)
images/             All images, named to match their page (e.g. project04.png)
```

Each activity/project gets **one card** on the home page (image, title,
one-line description) that links to **one detail page** with the fuller
write-up: a hero image, a description, and optionally a photo gallery,
an embedded video, or a code sample.

## Adding a new activity or project

The easiest way is to ask your AI assistant. Something like:

> Add a new project page for "Project 4: <name>". Here's my description:
> [*a paragraph about what I built and learned*]. My hero image is
> `images/project04.png`. Follow the pattern in AGENTS.md.

Under the hood, that means: copy `template.html` to `project04.html`, fill
in the image/title/description, delete whichever optional blocks (gallery,
video, code) don't apply, and add a matching card to `index.html`. See
[AGENTS.md](./AGENTS.md) for the exact recipe your assistant should follow —
worth skimming yourself too, so you can do it by hand if you ever need to.

Other things you can ask for once the basics are in place:
- *"Add a photo gallery to project04.html with these three images."*
- *"Embed my YouTube video <link> on project04.html."*
- *"Change the site's accent color to blue"* — this only requires editing
  `theme.css`, since both stylesheets pull their colors from there.

Remember: after any change, save your work (Setup, step 7) so it actually
reaches your live site.

## For AI assistants

See [AGENTS.md](./AGENTS.md) — it has the structural rules, the recipe for
adding pages, and the content guardrails to follow.
