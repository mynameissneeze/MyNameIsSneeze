# 🌸 GitHub Profile Guide for Complete Beginners 🌸

Don't worry if you've never used GitHub before! This guide is for anyone who wants to make a cute, decorated, or personalized GitHub profile.

You can use **Markdown + HTML together**, which is how people make fancy profiles with:

- ✨ GIFs
- 🖼️ Images
- 💜 Animated text
- 🎵 Music widgets
- 📊 Stats
- 🎀 Decorations
- 📁 Collection pages

Your GitHub profile is basically your own little webpage!

---

## 🚀 Quick Start: How to Make Your README (Step by Step)

1. **Create a new repository** on GitHub.
2. **Name it exactly the same as your username.** (If your username is `ExampleName`, the repo must be named `ExampleName/ExampleName`.)
3. Make sure the repository is set to **Public**.
4. Add a file called `README.md`.
5. Open the file and start writing/decorating using the Markdown and HTML tips below.
6. Click **Commit changes** to save. Your changes won't show up until you do this!
7. Visit your GitHub profile page to see the result.

---

## 📏 Headings (Big Text)

Headings are used for titles. The more `#` symbols you use, the smaller the text becomes.

| Code | Result |
|---|---|
| `# Biggest Heading` | Largest text |
| `## Large Heading` | Large text |
| `### Medium Heading` | Medium text |
| `#### Small Heading` | Smaller text |
| `##### Smaller Heading` | Even smaller |
| `###### Smallest Heading` | Smallest text |

---

## ✨ Text Styling

| Style | Code | Result |
|---|---|---|
| Bold | `**This is bold**` | **This is bold** |
| Italic | `*This is italic*` | *This is italic* |
| Bold + Italic | `***Both together***` | ***Both together*** |

---

## 📝 Lists

**Bullet list:**
```md
- Apple
- Banana
- Orange
```

**Numbered list:**
```md
1. First
2. Second
3. Third
```

---

## 📖 Spacing & Dividers

- Add empty space with `<br>` (one line) or `<br><br>` (two lines).
- Add a divider between sections with `---`.

---

## 🎀 Center Text

Wrap anything in the following tags to center it — works with text, images, GIFs, buttons, and banners:

```html
<p align="center">

Your text here

</p>
```

---

## 🖼️ Images & GIFs

The easiest way to add an image is to **drag and drop it directly into your README** — GitHub uploads it automatically.

Or use HTML:

```html
<img src="IMAGE URL">
```

**Resize an image** by adding a `width`:

```html
<img src="IMAGE URL" width="200">
```

Rough size guide:

| Width | Size |
|---|---|
| 50 | Tiny |
| 100 | Small |
| 200 | Medium |
| 400 | Large |
| 600 | Huge |

GIFs work exactly the same way:

```html
<img src="GIF URL" width="250">
```

## 💜 Animated Typing Text

Want your name or a message to "type itself"? Use the generator at:

https://readme-typing-svg.demolab.com/

Customize the font, color, size, speed, and alignment, then copy the code it gives you. Example:

```html
<img src="https://readme-typing-svg.demolab.com?font=Caveat&size=35&duration=1&pause=999999&color=FFD700&center=true&vCenter=true&width=600&lines=Hello!"/>
```

Common settings:

| Setting | What it does | Example |
|---|---|---|
| `font=` | Changes the font | `font=Caveat` |
| `size=` | Changes the text size | `size=35` |
| `color=` | Changes the color | `color=FFD700` |
| `lines=` | Sets the words (separate with `;` for multiple lines) | `lines=Hello!;Welcome;Thanks for visiting!` |

---

## 🌈 Colorful Text & Lettering

A popular trick is giving **each section its own color** instead of using one color for the whole page — you'll see this a lot on decorated profiles. It uses the same Typing SVG tool from above; you just change the `color=` value for every heading.

Example — two section headers with different colors:

```html
<img src="https://readme-typing-svg.demolab.com?font=Pacifico&size=24&duration=1&pause=999999&color=FF6B6B&center=true&vCenter=true&width=300&lines=Currently+Listening+To">
```

```html
<img src="https://readme-typing-svg.demolab.com?font=Pacifico&size=24&duration=1&pause=999999&color=9D4EDD&center=true&vCenter=true&width=300&lines=Kins">
```

Just swap the `color=` hex code (six characters, no `#`) for each section to build up a rainbow of differently-colored headers throughout your profile. Pick colors with HTML Color Codes or Adobe Color (linked below).

A few popular hex codes people use for this look:

| Color | Hex |
|---|---|
| Coral red | `FF6B6B` |
| Yellow | `FFD93D` |
| Green | `6BCB77` |
| Blue | `4D96FF` |
| Lavender | `B19CD9` |
| Purple | `9D4EDD` |
| Pink | `FF5DA2` |

---

## 🔗 Clickable Text & Images

**Clickable text:**
```md
[My Website](https://example.com)
```

**Clickable image** (great for social buttons, art pages, commission links):
```html
<a href="https://example.com">

<img src="IMAGE URL" width="200">

</a>
```

---

## 📂 Drop-Down (Collapsible) Sections

One of the coolest things you can add — people click to reveal hidden content:

```html
<details>

<summary>✨ Click Me!</summary>

Hidden stuff goes here! Pictures, GIFs, lists, text — anything!

</details>
```

You can put almost anything inside: images, GIFs, character info, art collections, favorite movies, commission examples, or long lists.

---

## 📁 "View Collection" Pages

This isn't a special button — it's just a link to another Markdown file in your repo.

**1. Create the extra page:**
1. Go to your repository.
2. Click **Add file** → **Create new file**.
3. Name it something like `Art.md`.
4. Add your content and save.

**2. Link to it from your README:**
```md
➡️ **[View Art](Art.md)**
➡️ **[View Characters](Characters.md)**
➡️ **[Commission Info](Commissions.md)**
```

---

## 💻 Code Blocks

To show code without GitHub changing it, wrap it in three backticks with the language name, e.g.:

````md
```html
<p>Your code here</p>
```
````

Tumblr is also great for finding graphics — try searching: `blinkies`, `pixel dividers`, `webcore graphics`, `stamps`, `favicons`, `website decorations`, `aesthetic graphics`.

---

## 🎵 Music & Discord Widgets

Want your profile to show live info like your current song or Discord status? These are called **widgets** — small cards that automatically update on your README.

### Spotify GitHub Profile

Shows your current song, artist, album cover, and Spotify activity.

Use: https://github.com/kittinan/spotify-github-profile

**How it works:**
1. Go to the Spotify GitHub Profile page.
2. Follow the setup instructions.
3. Connect your Spotify account.
4. Copy the code it generates.
5. Paste it into your `README.md`.

Example:
```md
# 🎵 Currently Listening To
Spotify Widget Here
```

💡 **Tip:** This updates automatically whenever you're listening to music — no manual updates needed.

### Lanyard Profile Readme (Discord Status)

Shows your online status, current game, music, and activity.

Use: https://github.com/Phineas/lanyard-profile-readme

**How it works:**
1. Turn on Discord Developer Mode: `Discord Settings` → `Advanced` → `Developer Mode`.
2. Copy your Discord ID: right-click your username → **Copy User ID**. It'll look like `123456789012345678`.
3. Join the Lanyard Discord server — this lets Lanyard read your public Discord activity.
4. Add the code it gives you to your README:
```md
[![Discord Presence](https://lanyard.cnrad.dev/api/YOUR_ID)](https://discord.com/users/YOUR_ID)
```
Replace `YOUR_ID` with your Discord ID.

### ⚠️ Widget Safety Tips

- Never share private tokens or passwords.
- Don't paste Client Secrets into your README.
- If something doesn't appear immediately, wait a few minutes.
- Make sure your accounts are connected correctly.

---

## 🎨 Profile Section Ideas

**About Me:**
```md
# 🌸 About Me

Hi! I'm ___!

I like:
- 🎨 Art
- 🎮 Games
- 🎵 Music
- 🌱 Nature
```

**Art gallery (using a drop-down):**
```html
<details>

<summary>🎨 My Art</summary>

<img src="IMAGE URL">

</details>
```

**Favorite games:**
```md
- 🎮 Minecraft
- 🌱 Stardew Valley
- ⭐ Roblox
- ⚔️ Destiny
```

**Commission info:**
```md
🌸 Commissions Open!

Prices:
- Headshot – $15
- Bust – $20
- Full Body – $30
```

**Social links:**
```md
🌸 Socials:
- Twitter
- Instagram
- Portfolio
```

**A common overall layout:**
```
✨ Banner
💜 Typing Name
🌸 About Me
🎨 Artwork
🎮 Favorites
🎵 Music
📊 Stats
🌐 Social Links
```

---

## 🎀 Cute Section Titles

**Section title ideas:**
```
✦ About Me ✦
୨୧ My Projects ୨୧
♡ Favorites ♡
🌸 Things I Like 🌸
🎨 My Artwork 🎨
🎮 Games I Play
🎵 Music Corner
💌 Contact Me
⭐ My Links ⭐
🍄 Fun Facts 🍄
```
## 🌐 Cool Websites to Decorate Your Profile

Aesthetic Bio Brackets (cute brackets/symbols): https://www.aestheticbio.net/p/bracket.html
<br>
Kaomoji (cute text faces): https://kaomoji.you/en/
<br>
Kawaii Emoji Combos: https://emojicombos.com/kawaii
<br>
Blinkie.net: https://blinkie-net.neocities.org/divider
<br>
Pixel Safari: https://pixelsafari.neocities.org/dividers/
<br>
Thuvien Webcore: https://thuvien.org/webcore/browse
<br>
Blinkies Cafe: https://blinkies.cafe
<br>
Adrian's Blinkie Collection: https://adriansblinkiecollection.neocities.org
<br>
Glitter Graphics: https://www.glitter-graphics.com

---
Good places to find GIFs: Giphy, Tenor, Tumblr, Pinterest.

---

## ❌ Common Beginner Mistakes

| Mistake | Wrong | Correct |
|---|---|---|
| Forgetting to close HTML tags | `<p>` Hello! | `<p>` Hello! `</p>` |
| Missing quotation marks | `<img src=image.png>` | `<img src="image.png">` |
| Forgetting the `>` | `<img src="image.png"` | `<img src="image.png">` |
| Forgetting the `/` in closing tags | `</p` | `</p>` |
| Using a local file path | `C:\Users\You\Pictures\image.png` | An uploaded image or hosted image URL |
| Forgetting `https://` | `www.example.com` | `https://www.example.com` |
| File name mismatches | Linking to `art.md` when the file is `Art.md` (GitHub is case-sensitive) | Match names exactly |
| Forgetting to commit | Edits made but not saved | Click **Commit changes** |
| Private repository | Repo set to Private | Set repo to **Public** |
| Oversized images | Huge image with no width set | Add `width="200"` (or adjust until it looks right) |

---

## 💡 Beginner Tips

- Save and commit often.
- Preview your profile after each change.
- Experiment — you can always edit your README later.
- Keep backups of your code.
- Mix Markdown and HTML together freely.
- Use spacing and dividers to keep sections organized.
- Don't be afraid to try new decorations.

---

# 🌸 Happy Decorating! 🌸
