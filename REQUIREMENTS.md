# Requirements for Pygameengine

This document outlines the requirements for running, developing, and extending Pygameengine.

---

## 1. Python Version

- Python 3.7 or higher is recommended.

---

## 2. Required Python Packages

- **Standard Library:**  
  The core engine relies primarily on Python's standard library (`os`, `json`, etc.).

- **Third-Party Dependencies:**  
  If any additional packages are required, please list them here or in `requirements.txt`.

---

## 3. Project Structure

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

## 4. Directory Details

- `data/accounts/`  
  Stores user account data, language selection, and save files.

- `data/lib/`  
  Contains reusable Python modules (`tools.py`, `boxgen.py`) used throughout the engine.

---

## 5. Language Packs

- Language files should be placed under the appropriate directory and follow the structure used in the engine.
- The engine expects language packs to contain all required prompt strings and menu items.

---

## 6. Usage

To run the engine:
```bash
python main.py
```

---

## 7. Platform Compatibility

- The engine is designed for terminal usage and should work on Windows, macOS, and Linux.
- File paths use `os.path`, but be cautious about Windows vs. Unix path separators in custom scripts.

---

## 8. Extending the Engine

- Implement your game logic in `game.main()`.
- Add new language packs as needed.
- Use the modular UI (`boxgen.pregen`) for additional menus and prompts.

---

## 9. Optional (Recommended) Tools

- [Git](https://git-scm.com/) for version control.
- [Visual Studio Code](https://code.visualstudio.com/) or any Python IDE for editing.

---

## 10. License

- See `LICENSE` file for details.

---

## 11. References

- Inspired by:  
  [pygamii](https://github.com/carlosmaniero/pygamii),  
  [scrap_engine](https://github.com/lxgr-linux/scrap_engine),  
  [pyplayscii](https://github.com/k2sebeom/pyplayscii),  
  [Bane-Of-Wargs](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs)

---
