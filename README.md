<div align="center">

<img width="1582" height="1092" alt="Mecha Chameleon Tools" src="https://github.com/user-attachments/assets/e0dbeffe-b591-4bf5-9fc0-0f047a545c3d" />

# Mecha Chameleon Tools

External ESP · Aimbot · Radar · Player Mod · Camouflage for **MECCA CHAMELEON** (UE5.6)

<img width="1213" height="793" alt="Preview" src="https://github.com/user-attachments/assets/512aafbb-8199-42e5-9313-f28249306a02" />

</div>

---

## Overview

A fully **external** overlay tool for MECCA CHAMELEON. All gameplay reads happen via
memory (pymem) — nothing is injected into the game's code. The camouflage system is the
only component that uses a small injected bridge DLL for in-game mesh painting.

> **Status:** `v1.0.0` is the latest stable release. The in-app updater will automatically deliver any future patches directly to you.

---

## Features

| Category | Capabilities |
|----------|-------------|
| **ESP** | Dot / 2D Box / Corner Box / Skeleton overlays, names, role labels (Hunter/Survivor), distance, snap lines, enemy-only filter, visible/not-visible coloring, invincible detection, per-role toggles, team filter, distance scaling, Draw All |
| **Health** | Health + shield bars, adjustable model height & Y offset |
| **Visuals** | Per-role Hunter/Survivor colors, invincible flag, Draw All actors, Disable Buried, Show Cursor, Background Geometry, line thickness & point size |
| **Radar** | External minimap with configurable size (80–400 px) and range (1000–50000) |
| **Aimbot** | Smooth aim assist, FOV circle, rebindable key, visible-only check |
| **Magnet** | Snap aim assist with independent FOV, strength slider, and key binding |
| **Player Mod** | Speed & jump multipliers, Teleport Collectible hotkey — *host only* |
| **Camouflage** | Bridge-based in-game paint system — paint / stop / review / unreview |

> **Note on ESP accuracy:** All ESP overlays are calculated in real time by reading
> game memory. When an opponent moves rapidly or is partially obscured, the position
> may show slight inconsistency on a single frame. The **snap line** is the most
> reliable indicator — it always connects screen-center to the player's resolved
> position, so follow the line when the box or dot appears to trail.

### Multi-Language

The UI ships in **9 languages** (EN, DE, FR, ES, CN, JP, KR, RU, TR), selectable from the
menu. The choice persists across sessions.

### In-App Updater

The menu checks GitHub Releases (including pre-releases) on startup and lets you download
and open the latest build directly — no need to revisit the Releases page manually.

---

## Quick Start

### Standalone (recommended — no Python required)
1. Download **`Mecha-Chameleon-Tools.exe`** from the [latest release](https://github.com/creepy-soumya/Mecha-Chameleon-Tools/releases/latest).
2. Launch MECCA CHAMELEON (windowed / borderless).
3. Run `Mecha-Chameleon-Tools.exe`.
**Requirements:** Windows 10/11, game running in windowed or borderless mode.

---

## Controls

| Key | Action |
|-----|--------|
| Insert / F1 | Toggle settings menu |
| Y | Teleport Collectible |
| MB4 | Magnet aim assist (hold) |
| F10 | Start painting (configurable) |
| F9 | Stop painting (configurable) |
| END | Quit application |
| Close button | Quit application |

### Settings Tabs

- **ESP** — Dot / Box / Corner Box / Skeleton toggles, Show Local, Names, Roles, Distance,
  Snap Lines, Team Filter, Enemy Only, Distance Scaling, dot radius, visible/not-visible colors.
- **HEALTH** — Health bar, shield bar, model height, Y offset.
- **VISUALS** — Per-role ESP toggles, Hunter/Survivor colors, invincible detection, Draw All
  actors, Disable Buried, Show Cursor, Background Geometry, line thickness & point size.
- **RADAR** — Enable/disable, size (80–400 px), range (1000–50000).
- **AIM/ASSIST** — Aimbot (enable, FOV circle, key, radius, smoothing, offset) and the Magnet
  aim-assist sub-section (key, FOV, strength).
- **PLAYER** — Player Mod toggle with Speed & Jump multipliers, Teleport Collectible key.
  *Host only.*
- **CAMOUFLAGE** — Paint, stop, review, and unreview your character mesh. Requires the game
  process running.



## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Game attach failed | Verify the game process is running before launching the tool |
| ESP shows nothing | Load into a match |
| Fewer players detected | Disable Team Filter |
| Snap lines not visible | Off-screen players draw lines to the screen edge |
| Aimbot not firing | Re-record the aim key |
| Radar not showing | Enable Radar in the RADAR tab |
| Player Mod not working | Must be the game host |

---



---

## Changelog

### v1.0.0
- **Camouflage engine updated** — new authenticated session protocol replaces the old
  loader-based injection (no more `bridge-loader.dll`). Dynamic port assignment,
  per-instance staging with automatic cleanup of stale bridge folders.
- **Config persistence fix** — settings now save next to the EXE when frozen, resolving
  a silent write failure inside the PyInstaller bundle directory.
- **ESP `bHidden` offset** updated for the latest game patch.
- **Bridge status** in the Camouflage tab now reliably transitions from "checking" to
  "Connected" or "Disconnected" (no more stuck label).

### v1.9.1.1-beta
- **UI redesign** — modern dark theme with accent palette, gradient controls, and a reorganized
  card-based menu (sidebar icons, grouped sections, primary Save / danger Close buttons).
- **ESP stability** — overlays now render from a coherent off-thread snapshot with player
  persistence, eliminating flicker, lag, and players disappearing during fast movement.
- **Localization** — added Russian (RU) and Turkish (TR); now 9 languages.
- **Updater** — in-app update checker/downloader added; `meccha_chameleon_tools.spec` now tracked
  so maintainers can rebuild.

### v1.9.1-beta
- In-app update checker/downloader.
- Build spec tracked in repo.
- Version source centralized in `updater.py`.

### v1.9.0-beta
- Camouflage reworked with a lighter bridge system (loader-based injection, port 50262).
- Simplified camouflage UI (Start / Stop / Review / Unreview).
- Native files moved into the `native/` subdirectory.

### v1.8.1
- Multi-language support (7 languages).
- Coherent dark theme with styled combo box popup, sliders, and scrollbars.

### v1.8.0
- Role detection (Hunter/Survivor), enemy-only filter, corner box.
- Visible/not-visible coloring, Load Config, END-key exit.

---

## Disclaimer

For educational and research purposes only. Use at your own risk.

## License & Attribution

This project incorporates code from [acentrist/MecchaCamouflage](https://github.com/acentrist/MecchaCamouflage)
(GPL-3.0). Full license text in `LICENSE.txt`.
