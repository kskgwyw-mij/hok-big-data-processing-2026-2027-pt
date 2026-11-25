"""Session 4 – environment check.

Run it in the terminal, once BEFORE and once AFTER activating your virtual environment:

    python session-04/check_env.py

It only reads information; it changes nothing on your machine.
"""
import importlib, os, platform, shutil, subprocess, sys
from pathlib import Path

OK, NO, INFO = "✓", "✗", "·"


def line(mark, label, value=""):
    print(f"  {mark} {label:<26} {value}")


print("\n== Python interpreter ==")
line(INFO, "Python version", platform.python_version())
line(INFO, "Executable", sys.executable)
line(INFO, "sys.prefix", sys.prefix)
line(INFO, "sys.base_prefix", sys.base_prefix)
in_venv = sys.prefix != sys.base_prefix
line(OK if in_venv else NO, "Inside a virtual env?", "yes" if in_venv else "NO – activate .venv first")
line(INFO, "Operating system", f"{platform.system()} {platform.release()} ({platform.machine()})")
line(INFO, "Logical CPUs", os.cpu_count())

if sys.version_info < (3, 10):
    line(NO, "Python too old", "use Python 3.12 (3.9 is end-of-life)")

print("\n== Packages (imported from THIS interpreter) ==")
for name in ["pandas", "pyarrow", "polars", "duckdb", "sklearn", "joblib", "pyspark", "psutil", "matplotlib"]:
    try:
        mod = importlib.import_module(name)
        line(OK, name, getattr(mod, "__version__", "?"))
    except ImportError:
        line(NO, name, "not installed in this environment")

try:
    import psutil
    vm = psutil.virtual_memory()
    line(INFO, "RAM total / available", f"{vm.total/1e9:.1f} GB / {vm.available/1e9:.1f} GB")
except ImportError:
    pass

print("\n== Java (only needed if you run Spark locally) ==")
java = shutil.which("java")
if java is None:
    line(INFO, "java", "not found – fine, Spark runs on Kaggle today")
else:
    out = subprocess.run([java, "-version"], capture_output=True, text=True).stderr
    first = next((l for l in out.splitlines() if "version" in l), out.strip()[:60])
    line(INFO, "java", first)

print("\n== Data folder ==")
data = Path(__file__).resolve().parent.parent / "data"
files = sorted(p.name for p in data.glob("*") if p.suffix in {".parquet", ".csv"})
line(OK if files else NO, str(data), ", ".join(files) if files else "empty – run: python get_data.py --months 2")
print()
