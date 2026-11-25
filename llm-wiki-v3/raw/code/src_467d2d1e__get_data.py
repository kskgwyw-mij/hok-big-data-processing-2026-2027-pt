"""Download NYC Yellow Taxi trip data (Parquet) and the taxi zone lookup into ./data.

Only uses the Python standard library, so it also runs before you created a virtual environment.

Usage:  python get_data.py            # 2024-01 .. 2024-06 (~300 MB) + taxi zone lookup
        python get_data.py --months 2 # what Session 4 needs (~100 MB)
"""
import argparse, pathlib, shutil, urllib.request

BASE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{y}-{m:02d}.parquet"
ZONES = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"


def download(url, f):
    print(f"↓ {url}")
    tmp = f.with_suffix(f.suffix + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": "hok-big-data-course"})
    with urllib.request.urlopen(req, timeout=120) as r, open(tmp, "wb") as fh:
        shutil.copyfileobj(r, fh, length=1 << 20)
    tmp.replace(f)                       # only complete files get the final name
    print(f"  {f.stat().st_size/1e6:.1f} MB")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--year", type=int, default=2024)
    p.add_argument("--months", type=int, default=6)
    a = p.parse_args()
    out = pathlib.Path(__file__).parent / "data"
    out.mkdir(exist_ok=True)
    for m in range(1, a.months + 1):
        f = out / f"yellow_tripdata_{a.year}-{m:02d}.parquet"
        if f.exists():
            print(f"✓ {f.name} already there"); continue
        download(BASE.format(y=a.year, m=m), f)
    zones = out / "taxi_zone_lookup.csv"
    if zones.exists():
        print(f"✓ {zones.name} already there")
    else:
        download(ZONES, zones)


if __name__ == "__main__":
    main()
