# Build Commands for Chameleon Tools

Below are the commands we discussed for building the project. You can run these from your PowerShell terminal in the project directory.

## 1. Build the C++ Runtime
Before running this, make sure you have installed the **Visual Studio Build Tools** and specifically selected the **"Desktop development with C++"** workload.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File runtime/scripts/build.ps1
```

## 2. Install Python Dependencies
Install PyInstaller along with the modules required by the tool (such as `pymem`, `PyQt5`, and `pywin32`) to prevent hidden import errors during the build.

```powershell
python -m pip install pyinstaller pymem PyQt5 pywin32
```

## 3. Build the Python Executable
Once the dependencies are installed, run this command to build your `.exe` file. The output will be placed in the `dist` folder.

```powershell
python -m PyInstaller --clean meccha_chameleon_tools.spec
```
