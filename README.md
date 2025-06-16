# Pygameengine
Ever wanted to make a game just in python console, but it looked awful? Well: now you can do it with a beatiful Ascii look
Pygameengine is a Python-based ASCII game engine designed for terminal-based games that require robust account, localization, and save management. It provides a modular system for user interaction, persistent data handling, and extensibility for building text-based games.

---

## Features

### 1. Multi-Language Support
- Dynamic language selection at startup.
- Language packs for localization of UI strings.
- Persistent storage of user language preference.

### 2. Account Management
- Supports creation and login of user accounts.
- PIN-based authentication with secure hashing.
- User account data stored as JSON files.

### 3. Save System
- Multiple saves per user, each with a custom name and unique ID.
- Save creation, selection, editing, renaming, deletion, and file path copying.
- Saves stored as individual JSON files for easy backup and transfer.
- Automatic slot management: always fills the lowest available ID.

### 4. User Interface
- Modular UI using `boxgen.pregen` for rendering menus, prompts, and info boxes.
- Supports colored UI elements and custom headings.
- Clear, structured prompts and error messages for better UX.

### 5. Extensibility & Architecture
- Modular code with utility libraries (`tools`, `boxgen`).
- Designed for easy feature expansion and game logic integration.
- Placeholder for main game logic (`game.main()`).

---

## How It Works

1. **Startup**: User selects a language. The choice is saved and used for all interface messages.
2. **Authentication**: Users create or enter a PIN to access their account. PINs are securely hashed.
3. **Save Management**: Users can create, select, rename, or delete saves. Save files are managed automatically.
4. **Menus & Prompts**: All user interaction is handled via modular, styled terminal boxes.

---

## Example Flow

1. On launch, select language from a menu.
2. If new user, create an account with a PIN; if returning, enter PIN to login.
3. Choose, create, or manage saves through a guided menu.
4. Proceed to game logic (to be implemented by you).

---

## Comparison with Other Python ASCII Game Engines

| Engine / Feature             | Python | Terminal UI | Modular Menus/Prompts | Account System | Multi-language Support | PIN Authentication | Save System      | File-based Persistence | Extensible Architecture | Made for Text-Based Game |
|:---------------------------:|:------:|:-----------:|:---------------------:|:--------------:|:---------------------:|:------------------:|:-----------------:|:----------------------:|:-----------------------:|:------------------------:|
| **Pygameengine**            | ✅       | ✅          | ✅                    | ✅             | ✅                    | ✅                 | 🔷 Advanced       | JSON                   | ✅                      | ✅                       |
| **pygamii**                 | ✅       | ✅          | ✅                    | ❌             | 🟡                    | ❌                 | 🔹 Basic          | JSON                   | ✅                      | ✅                       |
| **scrap_engine**            | ✅       | ✅          | ✅                    | ❌             | ❌                    | ❌                 | 🔹 Basic          | JSON                   | ✅                      | ✅                       |
| **pyplayscii**              | ✅       | ✅          | 🟡                    | ❌             | ❌                    | ❌                 | 🔹 Basic          | JSON                   | ✅                      | ✅                       |
| **Bane-Of-Wargs**           | ✅       | ✅          | ✅                    | ❌             | ❌                    | ❌                 | 🔷 Advanced       | JSON                   | ✅                      | ✅                       |
| **Asciin.py**               | ✅       | ✅          | 🟡                    | ❌             | ❌                    | ❌                 | ❌                | ❌                     | ✅                      | ✅                       |
| **AsciiEngine**             | ❌(CSS,C)| ✅          | 🟡                    | ❌             | ❌                    | ❌                 | ❌                | ❌                     | ✅                      | ✅                       |
| **roguelike-ascii-vs-pygame** | ✅     | ✅          | ✅                    | ❌             | ❌                    | ❌                 | 🔹 Basic          | JSON                   | 🟡                      | Example Only             |

| Symbol   | Meaning            |
|:--------:|:-------------------|
| ✅       | Yes                |
| ❌       | No                 |
| 🟡       | Partial/Kinda      |
| 🔷       | Advanced           |
| 🔹       | Basic              |

---

## Getting Started

1. Clone this repository or downlaod the most recent release.
2. Install requirements if any still needed (see [requirements.md](requirements.md)).
3. Run the main script:
   ```bash
   python main.py
   ```
4. Follow terminal prompts for language, PIN, and save selection, so you have your base settings
5. Program your game in `game.py` (How you use the librarys is shown in the _soon coming_ **WIKI**)
---

## Folder Structure

```
data/
  accounts/
    ackknow.json
    sellang.json
    saves/
      s1.json
      s2.json
  lib/
    tools.py
    boxgen.py
main.py
```

---

## Extending the Engine

- Implement your game logic in the `game.main()` method.
- Add or modify language packs in the `data/lang/` directory.
- Use `boxgen.pregen` for custom UI elements and prompts.

---

## License

Check [LICENSE.md](LICENSE.md) out!

## Credits

- this Project has no Inspirations!
- this Project was made after long long time of thinking, how to do it the best.
- README.md,LICENSE.md and REQUIREMENTS.md were generatet by AI on purpose with modifications
