import os
import sys
import re
import subprocess
import shutil

UPDATER_FILE = os.path.join("meccha_chameleon_tools", "updater.py")
SPEC_FILE = "meccha_chameleon_tools.spec"

def update_file(filepath, pattern, replacement):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = re.sub(pattern, replacement, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    if len(sys.argv) < 2:
        print("Usage: python build_release.py <version>")
        print("Example: python build_release.py 1.0.1")
        sys.exit(1)
        
    new_version = sys.argv[1].lstrip("v") # Remove 'v' if user typed v1.0.1
    
    print(f"[*] Bumping version to {new_version}...")
    
    # 1. Update updater.py
    if os.path.exists(UPDATER_FILE):
        update_file(
            UPDATER_FILE, 
            r'APP_VERSION\s*=\s*".*"', 
            f'APP_VERSION = "{new_version}"'
        )
        print(f"  [+] Updated {UPDATER_FILE}")
    else:
        print(f"  [-] Error: Could not find {UPDATER_FILE}")
        sys.exit(1)

    # 2. Update .spec file to output the executable with the version name
    # e.g., Mecha-Chameleon-Tools-v1.0.1.exe
    exe_name = f"Mecha-Chameleon-Tools-v{new_version}"
    if os.path.exists(SPEC_FILE):
        update_file(
            SPEC_FILE,
            r"name\s*=\s*'Mecha-Chameleon-Tools.*',",
            f"name='{exe_name}',"
        )
        print(f"  [+] Updated {SPEC_FILE} output name to {exe_name}")
    else:
        print(f"  [-] Error: Could not find {SPEC_FILE}")
        sys.exit(1)
        
    # 3. Clean up old build/dist directories to prevent caching issues
    print("[*] Cleaning old build directories...")
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    # 4. Run PyInstaller
    print("[*] Running PyInstaller...")
    result = subprocess.run([sys.executable, "-m", "PyInstaller", "--clean", SPEC_FILE])
    
    if result.returncode == 0:
        print("\n" + "="*50)
        print(f"[SUCCESS] Build complete!")
        print(f"Your executable is ready at: dist/{exe_name}.exe")
        print("="*50)
    else:
        print("\n[ERROR] PyInstaller build failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
