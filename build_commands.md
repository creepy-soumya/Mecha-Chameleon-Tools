# Build Commands for Chameleon Tools

Below are the commands we discussed for building the project. You can run these from your PowerShell terminal in the project directory.

## 1. Build the C++ Runtime
Before running this, make sure you have installed the **Visual Studio Build Tools** and specifically selected the **"Desktop development with C++"** workload.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File runtime/scripts/build.ps1
```

py bridge artifacts into the package
Copy-Item "runtime\.build\bin\meccha-camouflage.exe" "meccha_chameleon_tools\meccha-camouflage.exe" -Force
Copy-Item "runtime\.build\bin\runtime-bridge.dll"     "meccha_chameleon_tools\meccha-xenos-bridge.dll" -Force
Copy-Item "runtime\.build\bin\runtime-injector.exe"   "meccha_chameleon_tools\meccha-xenos-injector.exe" -Force


## 2. Install Python Dependencies
Install PyInstaller along with the modules required by the tool (such as `pymem`, `PyQt5`, and `pywin32`) to prevent hidden import errors during the build.

```powershell
python -m pip install pyinstaller pymem PyQt5 pywin32
```

## 3. Build the Python Executable

**IMPORTANT:** Always use `build_release.py` to build — this bumps the version number in the code before compiling. NEVER run PyInstaller directly or the in-app version will stay as `1.0.0` forever.

Replace `1.0.3.7` with the actual version you want to release:

```powershell
python build_release.py 1.0.3.7
```

This script will automatically:
1. Update the version in `updater.py` to match the release tag
2. Update the `.spec` output filename to `Mecha-Chameleon-Tools-v1.0.3.7.exe`
3. Clean old build artifacts
4. Run PyInstaller

The final `.exe` will be in the `dist/` folder.

## 4. After Build - Upload to GitHub

Create a new GitHub Release with:
- **Tag:** `v1.0.3.7`
- **Asset 1:** `dist/Mecha-Chameleon-Tools-v1.0.3.7.exe`
- **Asset 2 (optional):** `meccha_chameleon_tools/meccha-camouflage.exe`

The in-app updater will then detect the new version and download the correct `.exe` automatically.
