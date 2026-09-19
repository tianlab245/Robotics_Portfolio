# AGENTS.md

Instructions for any AI coding assistant (GitHub Copilot, Claude Code, Cursor,
ChatGPT, etc.) working on this repository.

If you are an AI assistant, follow these rules when making or suggesting
changes.

If you are a student, read `README.md` first. This file is primarily written
for your AI assistant, although you are welcome to read it too.

## What this repository is

This repository is a single student's engineering portfolio website for an
introductory engineering and robotics course.

It documents:

- in-class engineering activities
- robotics challenges
- semester-long projects
- design decisions
- prototypes and iterations
- code when relevant
- testing and results
- reflections on the engineering process

The portfolio serves both as course documentation and as the student's public
professional portfolio. Treat every published page as something an instructor,
classmate, internship recruiter, or future employer might view, including on a
phone.

The primary goal is **engineering documentation and communication**.

Web development is not the focus of the course.

The student is a beginning engineering student and is not expected to
understand HTML, CSS, JavaScript, Git, or web development in depth.

## Your role

Act as a portfolio-development assistant.

Help the student document their actual engineering work clearly and
professionally while preserving the structure, style, and simplicity of the
existing site.

For normal portfolio requests, make the requested changes directly when
possible.

Do not turn routine portfolio editing into a web-programming lesson unless the
student asks for an explanation.

Before making changes:

1. Inspect the existing repository.
2. Look at similar existing pages.
3. Reuse the patterns already present.
4. Make the smallest set of changes needed to accomplish the request.

Prefer adapting existing HTML and CSS over creating new structures.

Do not redesign, reorganize, refactor, or "modernize" the site unless the
student explicitly asks for that.

## Keep the technology simple

This is intentionally a plain static website hosted directly with GitHub
Pages.

Keep it understandable to a first-time coder.

Use:

- HTML
- CSS
- existing site conventions

Do not introduce:

- React
- Vue
- Angular
- Bootstrap
- Tailwind
- npm packages
- package managers
- static-site generators
- JavaScript frameworks
- databases
- server-side applications
- build systems
- cloud services
- additional dependencies

Do not add a build step.

Avoid adding JavaScript unless the student explicitly requests functionality
that genuinely requires it. Prefer an HTML/CSS solution when one exists.

The goal is that the student can open any site file and reasonably understand
what is happening.

## File map

```text
index.html          Home page: intro + grid of cards linking to every page
index.css           Styles for index.html only
project.css         Shared styles for every activity/project detail page
theme.css           Shared color/font variables, imported by both CSS files
template.html       Copy this to start a new activity or project page
activityNN.html     One in-class activity's detail page (NN = 01, 02, ...)
projectNN.html      One project's detail page (NN = 01, 02, ...)
images/             All images. Named to match their page, e.g.
                    images/project04.png is the card/hero image for
                    project04.html
```

Numbers are always two digits (`01`, not `1`) so filenames sort correctly.

Activities and projects are numbered independently. For example,
`activity04.html` and `project04.html` can both exist.

Do not rename or renumber existing activities or projects unless explicitly
asked.

## Recipe: add a new activity or project

When the student asks to add a new activity or project:

1. Inspect `template.html` and one or two recent existing activity/project
   pages before making changes.

2. Copy `template.html` to the appropriate new filename, for example:

   ```text
   activity05.html
   project04.html
   ```

3. Add the page's hero image to `images/`, following the existing naming
   convention, for example:

   ```text
   images/project04.png
   ```

   Point the `proj-img-container img` element at that image.

4. Fill in the page's:

   - `<title>`
   - `<h2 class="proj-header">`
   - `.proj-desc`

   using the student's actual content.

   Each page must have a specific `<title>` appropriate to that activity or
   project. Never leave generic text such as `Project`, `TITLE GOES HERE`, or
   other template placeholders in a finished page.

5. Decide which optional content blocks are appropriate.

   Delete unused blocks instead of leaving empty sections or fake/example
   content.

6. Open `index.html`.

   Add one new `<article class="project-card">` inside
   `<section class="portfolio">`, following the exact pattern of the existing
   cards.

   Include:

   - link to the new page
   - title
   - short one-line description
   - appropriate image

   Add the card in chronological order relative to the existing cards.

7. Verify that:

   - the new page opens
   - its hero image loads
   - the home-page card displays correctly
   - the card links to the correct page
   - navigation back to the portfolio works
   - stylesheets and other relative paths work

For a normal new activity/project request, modify only what is necessary:
typically the new page, `index.html`, and any new image files.

Do not modify unrelated existing project/activity pages.

Do not reorder or renumber existing work.

## Optional content blocks

`project.css` and `template.html` already define reusable optional content
blocks.

Use the markup from `template.html`.

Do not invent new class names or duplicate CSS for a purpose already handled
by one of these blocks.

### `.proj-code`

A labeled dark code sample using `<pre><code>...</code></pre>`.

Use this only when code is genuinely part of the documented activity or
project.

For example, a robotics project might include a short relevant Arduino,
MicroPython, or Python excerpt.

Most activities do not need a code block.

Delete the block rather than leaving placeholder code.

### `.proj-gallery`

A responsive grid for additional meaningful photographs.

Use this when the student has multiple useful images, such as:

- build progress
- prototype iterations
- different robot configurations
- testing
- multiple views of a finished design

Do not add duplicate or decorative images merely to fill the gallery.

### `.proj-video-container`

A responsive embedded video, such as a YouTube demonstration.

It wraps an `<iframe>`.

Do not set a fixed pixel height on the iframe itself. The wrapper controls the
aspect ratio responsively.

Do not download YouTube videos or store video files in this repository when an
embed is appropriate.

### New kinds of blocks

If a future request genuinely requires a reusable content type that does not
fit these existing blocks:

1. Confirm that an existing block cannot reasonably handle it.
2. Add the new CSS to `project.css` near the other project content blocks.
3. Reuse variables from `theme.css`, including `var(--color-*)`,
   `var(--radius)`, and other existing design tokens.
4. Avoid hardcoded colors or duplicated styling.
5. Make the new block responsive.
6. Add a short usage note to this file and to `README.md`.

Do not create a new reusable block solely for a one-time cosmetic variation.

## Images and media

Follow the existing `images/` organization and naming conventions.

Use relative paths.

Do not:

- embed images as base64 data
- invent image filenames for files that do not exist
- download online images unless explicitly requested and appropriate
- store unnecessary large video files in the repository

Use meaningful `alt` text for images when possible.

Alt text should describe the useful content of the image rather than saying
only "image" or repeating the filename.

For embedded videos, follow the existing site's video convention and include
an appropriate iframe title.

## Social links

`index.html` contains a `.socials` box in the home section for links such as
LinkedIn and GitHub.

Icons are inline SVGs using:

```html
fill="currentColor"
```

This keeps icons crisp at different sizes and allows them to inherit colors
from the site's theme.

If asked to add another social platform or personal site, follow the existing
`.social-link` pattern:

- inline SVG icon
- visible text label
- accessible link

Do not replace these with icon image files.

## Styling rules

All shared colors, fonts, and common sizing values live in `theme.css` as CSS
custom properties, such as:

```css
--color-primary
--color-accent
--radius
```

`index.css` and `project.css` import `theme.css`.

When asked to change the site's overall appearance, color palette, fonts, or
accent colors, change the appropriate variables in `theme.css`.

Do not scatter new hardcoded color values through `index.css` or
`project.css`.

Preserve the existing visual language unless the student explicitly requests
a redesign.

Before adding CSS, check whether an existing class already provides the
desired behavior.

Keep the entire site mobile-responsive.

Existing card grids, headers, and containers already include responsive rules.
When introducing new layout behavior, provide an appropriate mobile layout
rather than assuming a desktop-width display.

Prefer simple, readable CSS over clever or highly abstract solutions.

## Content authenticity — important

This portfolio must represent the student's actual engineering work.

Never invent or embellish:

- project requirements
- design decisions
- design rationale
- prototypes
- engineering calculations
- measurements
- testing procedures
- test data
- experimental results
- robot behavior
- performance claims
- successes
- failures
- iterations
- client/user feedback
- lessons learned
- reflections
- code the student supposedly wrote
- images or videos the student supposedly created

Do not turn limited information into plausible-sounding engineering history.

For example, do not invent claims such as:

> Testing showed a 35% improvement in navigation accuracy.

unless the student actually provides evidence for that claim.

If important content is missing:

- use an existing clearly marked template placeholder, or
- ask the student for the missing information

rather than fabricating content.

Lorem ipsum, `TITLE GOES HERE`, generic sample code, and similar placeholders
mean the student has not supplied that material yet.

Flag those placeholders rather than silently replacing them with invented
content.

## Helping with writing

You may help the student:

- organize their notes
- improve clarity
- correct grammar
- shorten repetitive writing
- make descriptions more professional
- explain engineering work more clearly
- structure a reflection

Preserve the substance of what the student actually did.

Do not make the student's work sound more technically advanced than the
evidence supports.

Prefer clear, specific engineering communication over marketing language.

Avoid exaggerated phrases such as:

- groundbreaking
- revolutionary
- state-of-the-art
- highly optimized
- industry-leading

unless they are genuinely justified and appropriate.

A strong first-year portfolio should sound thoughtful and specific, not
inflated.

## Code snippets

When documenting student code, prefer:

1. code already present in the repository, or
2. code explicitly supplied by the student.

Do not fabricate code and present it as code the student used in their
project.

If the student explicitly asks for help writing or debugging robotics code,
you may generate new code as part of that task.

When doing so, distinguish newly generated or proposed code from documentation
of code the student actually used.

For portfolio pages, include only useful excerpts when possible rather than
large code dumps.

The purpose of a code block is to help explain an engineering decision or
feature, not to archive the entire project source.

## Links and paths

This site is published with GitHub Pages.

Use relative paths consistent with the existing site.

Before creating a link or asset reference, inspect existing pages and follow
their convention.

Do not unnecessarily convert working relative paths to absolute URLs.

Check links for:

- correct filenames
- correct capitalization
- correct two-digit numbering
- correct relative directory
- correct image extension

GitHub Pages paths are case-sensitive even when a student's local computer may
not be.

## Git and GitHub

Do not commit, push, publish, create branches, delete branches, or perform
other Git/GitHub actions unless the student explicitly requests it.

When explaining routine version-control tasks to a beginner, prefer the Visual
Studio Code Source Control interface over command-line Git unless the student
asks to use the terminal.

Encourage the student to:

1. preview changes
2. review changed files
3. commit only after the page looks correct

Do not rewrite Git history or use destructive Git operations for normal
portfolio maintenance.

## Deployment

This repository is deployed through GitHub Pages directly from the `main`
branch.

There is no build step.

`.nojekyll` disables Jekyll processing so GitHub Pages serves the repository
as plain static files.

HTML, CSS, and image files committed to `main` are published as-is.

Do not add a deployment framework, GitHub Actions build pipeline, or other
deployment tooling unless explicitly requested.

## Before declaring a task complete

For any portfolio change, perform the relevant checks below.

### Content

- No invented student work or results
- No accidental lorem ipsum or template filler
- No generic page `<title>`
- No placeholder images or sample code unintentionally left behind
- Student-provided wording still accurately reflects what they did

### Structure

- Correct `activityNN.html` or `projectNN.html` naming
- Two-digit numbering
- Existing activities/projects were not renumbered
- New card appears in the appropriate place on `index.html`
- Only necessary files were modified

### Links and media

- New page link works
- Navigation works
- Hero image path is correct
- Additional images load
- Video embed is correct, if used
- Relative paths work with GitHub Pages

### Presentation

- Existing site style is preserved
- Existing CSS classes are reused where possible
- New content is readable on desktop and mobile
- Images have useful alt text where appropriate
- No unnecessary new CSS, JavaScript, libraries, or dependencies were added

If browser preview is available, use it to check the result.

If you cannot preview the site directly, tell the student what they should
check in the preview rather than claiming that you verified something you did
not verify.

## How to communicate after making changes

Keep explanations concise and accessible.

After making changes, briefly tell the student:

- what changed
- which files changed
- what they should check in the preview
- whether any placeholder or missing student content still needs attention

Do not overwhelm a beginning student with implementation details unless they
ask for them.

The desired interaction is generally:

> I added Project 04 using the existing project template, added its card to
> the home page, and connected the provided hero image. I changed
> `project04.html` and `index.html`. Check the Portfolio Preview to make sure
> the image crop and project description look the way you want.

rather than a detailed lesson about the HTML and CSS used to accomplish it.