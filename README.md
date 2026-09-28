<div align="center">

# Banozz

### I run a team of AI agents that builds, tests and ships real software.

**Open to work:** AI automation and AI operations roles. Remote, English. Email below.

Found a bug or have an idea? Open an issue or send a PR.

<a href="mailto:svenmedina07@gmail.com"><img alt="Email: get in touch" src="https://img.shields.io/badge/-Get%20in%20touch-7c3aed?style=for-the-badge&labelColor=5b21b6&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyLjI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxNiIgeD0iMiIgeT0iNCIgcng9IjIiLz48cGF0aCBkPSJtMjIgNy04Ljk3IDUuN2ExLjk0IDEuOTQgMCAwIDEtMi4wNiAwTDIgNyIvPjwvc3ZnPg%3D%3D"></a>
<a href="https://x.com/banozz_"><img alt="X: @banozz_" src="https://img.shields.io/badge/-%40banozz__-7c3aed?style=for-the-badge&labelColor=5b21b6&logo=x&logoColor=white"></a>
<a href="https://shipper.club"><img alt="Shipper Club member" src="https://img.shields.io/badge/-Shipper%20Club%20member-7c3aed?style=for-the-badge&labelColor=5b21b6&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyLjI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik00LjUgMTYuNWMtMS41IDEuMjYtMiA1LTIgNXMzLjc0LS41IDUtMmMuNzEtLjg0LjctMi4xMy0uMDktMi45MWEyLjE4IDIuMTggMCAwIDAtMi45MS0uMDl6Ii8%2BPHBhdGggZD0ibTEyIDE1LTMtM2EyMiAyMiAwIDAgMSAyLTMuOTVBMTIuODggMTIuODggMCAwIDEgMjIgMmMwIDIuNzItLjc4IDcuNS02IDExYTIyLjM1IDIyLjM1IDAgMCAxLTQgMnoiLz48cGF0aCBkPSJNOSAxMkg0cy41NS0zLjAzIDItNGMxLjYyLTEuMDggNSAwIDUgMCIvPjxwYXRoIGQ9Ik0xMiAxNXY1czMuMDMtLjU1IDQtMmMxLjA4LTEuNjIgMC01IDAtNSIvPjwvc3ZnPg%3D%3D"></a>

</div>

---

## Shipped

| Project | What it does | Type |
| :--- | :--- | :--- |
| **[hermes-context](https://github.com/banozz0/hermes-context)** | My Hermes agents work in Discord threads, and nothing told me which one was about to run out of context. Now every session sits in the menu bar: how full its context is, and whether it's working, waiting on me or idle. Keeps a private history; never stores a message. One-line install. | `macOS app` |
| **[telegram-tools](https://github.com/banozz0/telegram-tools)** | Telegram buries the IDs everything else needs, and makes a few jobs oddly hard. This tool makes them simply accessible via CLI — emptying a topic, exporting a thread, editing your bot. Type the tool's name and a menu opens. | `cli tool` |
| **[discord-tools](https://github.com/banozz0/discord-tools)** | Same idea, your Discord bot. One token in, and the server answers from the terminal — channels, threads, search, export. | `cli tool` |
| **[acca-tracker](https://github.com/banozz0/acca-tracker)** | Photo of a bet slip in. Every leg parsed and confirmed, then tracked from public scores — alive, dead, won. It reports; it never advises. | `agent skill` |
| **[Ghostex onboarding](https://github.com/banozz0/ghostex-onboarding-prototypes)** | The first-run flow every new Ghostex user now sees. I designed it and built the clickable prototypes it was coded from: concept to final, React and WebGL. [Try it live](https://banozz0.github.io/ghostex-onboarding-prototypes/). | `design · prototype` |

Both CLIs follow the same design: local-first, no account, nothing phoned home.

## Contributed to

| Project | What I did |
| :--- | :--- |
| **[Ghostex](https://github.com/maddada/Ghostex)**<br>`Rust · macOS` | [44 merged PRs](https://github.com/maddada/Ghostex/pulls?q=is%3Apr+author%3Abanozz0+is%3Amerged). Built the Bots space: a sidebar mode for your Hermes agents, a feed of every cron run they deliver, and Hermes chats that name the bot, show its context and switch models. Built out the Kanban board — custom columns, tag filtering, lane sorting, persistent view preferences — plus agent session dispatch, picking a worker's model and effort at launch, and a model pick for one session only. Also Global Actions, worktree renaming, and fixes across chat, worktrees and the CEF panes. Designed the [ghostex.dev](https://ghostex.dev) landing page that's live now (maddada built it), and the app's [first-run onboarding](https://github.com/banozz0/ghostex-onboarding-prototypes). |
| **[beads](https://github.com/gastownhall/beads)**<br>`Go` | Added the `comment`, `comments` and `note` MCP tools, so an agent can write back to the card it's working. |
| **[Hermes Agent](https://github.com/NousResearch/hermes-agent)**<br>`Python` | [In review](https://github.com/NousResearch/hermes-agent/pull/112321): `skill_manage` follows symlinked skill folders, with rollback and ownership staying on the link. |
| **[Ghostex Extensions](https://github.com/maddada/Ghostex-extensions)**<br>`TypeScript` | Contributed the Canvas extension, now [drawing with real Excalidraw](https://github.com/maddada/Ghostex-extensions/pull/2). |
| **[Sideshow](https://github.com/modem-dev/sideshow)**<br>`TypeScript` | In review: [download a surface as the file it came from](https://github.com/modem-dev/sideshow/pull/266), [markdown tables that scroll instead of splitting words](https://github.com/modem-dev/sideshow/pull/267), and [an opt-in wide layout for wide monitors](https://github.com/modem-dev/sideshow/pull/268). |

<details>
<summary><b>All 44 merged Ghostex PRs</b></summary>

**Bots space and Hermes**
- [#167](https://github.com/maddada/Ghostex/pull/167) Bots: a sidebar mode for your Hermes agents, one row per profile
- [#169](https://github.com/maddada/Ghostex/pull/169) Bot automations: a feed of every Hermes cron run
- [#163](https://github.com/maddada/Ghostex/pull/163) Hermes chats name the bot, show its context and switch models
- [#176](https://github.com/maddada/Ghostex/pull/176) Bot space patch: Hermes sessions keep their status, chat and name
- [#178](https://github.com/maddada/Ghostex/pull/178) Hermes chat shows what its terminal shows; `/compress` works like `/compact`
- [#179](https://github.com/maddada/Ghostex/pull/179) A woken Hermes session resumes under its own profile
- [#114](https://github.com/maddada/Ghostex/pull/114) Recognize Hermes composers with a profile-name prompt

**Kanban board and dispatch**
- [#104](https://github.com/maddada/Ghostex/pull/104) Filter the board by tag
- [#105](https://github.com/maddada/Ghostex/pull/105) Draw the board's own custom statuses as columns
- [#106](https://github.com/maddada/Ghostex/pull/106) Manage custom columns from the board
- [#85](https://github.com/maddada/Ghostex/pull/85) Lane sorting with directions and persistent view preferences
- [#84](https://github.com/maddada/Ghostex/pull/84) Show assignee and creator on cards
- [#90](https://github.com/maddada/Ghostex/pull/90) Start-work dispatch endpoint and CLI verb
- [#91](https://github.com/maddada/Ghostex/pull/91) Start work with the agent a card is assigned to
- [#116](https://github.com/maddada/Ghostex/pull/116) Start-work puts the worker in the named project, not the newest one
- [#108](https://github.com/maddada/Ghostex/pull/108) Let an agent link its own session to a card
- [#87](https://github.com/maddada/Ghostex/pull/87) Heal card conversation links, add Resume, share links across board mounts
- [#111](https://github.com/maddada/Ghostex/pull/111) Deliver card conversation links to the Kanban page
- [#86](https://github.com/maddada/Ghostex/pull/86) Mouse-grabbable board and dialog scrollbars
- [#74](https://github.com/maddada/Ghostex/pull/74) Keep an established issue prefix when a board is shared between projects

**Agents and chat**
- [#138](https://github.com/maddada/Ghostex/pull/138) Pick a worker's model and effort at launch
- [#147](https://github.com/maddada/Ghostex/pull/147) Apply a model pick to one session without changing the default
- [#150](https://github.com/maddada/Ghostex/pull/150) A wake never resumes another project's Claude conversation
- [#151](https://github.com/maddada/Ghostex/pull/151) Restore-wake only on return to a project, never over a requested session
- [#122](https://github.com/maddada/Ghostex/pull/122) Slash commands sent from chat keep their output after a reload
- [#121](https://github.com/maddada/Ghostex/pull/121) Show Codex local command transcripts
- [#113](https://github.com/maddada/Ghostex/pull/113) Skip the draft handoff for agents launched through a user hop
- [#100](https://github.com/maddada/Ghostex/pull/100) Per-session Verbose toggle in the composer

**Actions, worktrees and settings**
- [#79](https://github.com/maddada/Ghostex/pull/79) Store Global Actions in gxserver
- [#80](https://github.com/maddada/Ghostex/pull/80) Render Global Actions in the tab strip
- [#88](https://github.com/maddada/Ghostex/pull/88) Global Actions on project rows, updated instantly
- [#75](https://github.com/maddada/Ghostex/pull/75) Flagged quick actions on sidebar project rows
- [#94](https://github.com/maddada/Ghostex/pull/94) Rename a worktree's folder and branch from the sidebar
- [#93](https://github.com/maddada/Ghostex/pull/93) Mount a configurable folder beside each project's docs
- [#81](https://github.com/maddada/Ghostex/pull/81) Global Defaults for project settings
- [#102](https://github.com/maddada/Ghostex/pull/102) One web-link destination, and a settings rail that shows every section
- [#101](https://github.com/maddada/Ghostex/pull/101) Dock the command pane on the right
- [#76](https://github.com/maddada/Ghostex/pull/76) Optional background image behind terminal panes

**Desktop and build fixes**
- [#78](https://github.com/maddada/Ghostex/pull/78) Keep the live terminal when a command tab moves to Agents
- [#92](https://github.com/maddada/Ghostex/pull/92) Resolve native CEF entries on the dev server
- [#110](https://github.com/maddada/Ghostex/pull/110) Every CEF first responder owns the paste hotkey
- [#117](https://github.com/maddada/Ghostex/pull/117) Render the dialog layer so alert dialogs appear
- [#89](https://github.com/maddada/Ghostex/pull/89) Repair the cargo test build
- [#107](https://github.com/maddada/Ghostex/pull/107) Point submodule error hints at the right paths

</details>

## What I run

One person, a team of agents. Every job is a card on a shared board, and nothing counts as done until it has passed its tests and a separate reviewer agent has checked it. I write the specs, make the calls and approve anything risky. Scheduled jobs and nightly backups run on their own.

<!-- diagram:start -->
<details>
<summary><b>How a job moves from spec to done</b></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agents-dark.svg">
  <img alt="How a job moves from spec to done. 1. Me: Specs, decisions, approvals. 2. Shared task board: Every job is a card. 3. In parallel, Hermes agents: Always on, reachable from Discord and Telegram (Harry: planning and triage; Dobby: runs the system; Researcher: sourced research; Content: drafts posts); and Builders: Claude Code workers in Ghostex build and document. 4. Tested: Tests, builds, checked in the real app. 5. Reviewed: A separate reviewer agent checks every finished card. 6. Done. Failed test or review: back to the board." src="assets/agents-light.svg">
</picture>
</details>
<!-- diagram:end -->

The tools it runs on:

| Tool | What it's for |
| :--- | :--- |
| **Claude Code** | Where the building happens, from brainstorming an idea to the shipped product, with plenty of bug fixing in between. |
| **Codex** | Quick patches — and the provider my Hermes agents use. |
| **Hermes Agent** | The always-on half: memory, skills and scheduled jobs I can reach from Telegram or Discord when I'm nowhere near a desktop. |
| **Ghostex** | The ADE every agent runs in. Most of my merged PRs are in it, which should tell you how much I use it. |


<p align="center"><img alt="Banozz's GitHub stats" src="https://github-stats-extended.vercel.app/api?username=banozz0&show_icons=true&hide_border=true&bg_color=00000000&title_color=8B5CF6&icon_color=EF4444&text_color=888888&ring_color=8B5CF6"></p>
