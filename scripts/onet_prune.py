import json
from pathlib import Path

# Directories
RAW_DIR = Path("_data")
OUT_DIR = Path("_data/onet")
OUT_DIR.mkdir(exist_ok=True)

# Your anchor SOC codes
anchor_soc = {
    "11-3121.00",
    "13-1071.00",
    "13-1111.00",
    "13-1082.00",
    "13-1151.00",
    "11-3131.00",
    "15-2051.00",
    "19-3032.00",
    "15-2041.00",
    "15-1299.03"
}

print(f"Anchor SOC codes: {len(anchor_soc)}")

# Step 1: Expand via Related Occupations
related_soc = set()

with open(RAW_DIR / "related_occupations.json", "r", encoding="utf-8") as f:
    related_data = json.load(f)["row"]  # <-- IMPORTANT: rows live under "row"

for entry in related_data:
    base = entry.get("onetsoc_code")
    rel = entry.get("related_onetsoc_code")

    # If the base SOC is one of your anchors, add the related SOC
    if base in anchor_soc:
        related_soc.add(rel)

# Combine anchor + related SOC codes
expanded_soc = anchor_soc.union(related_soc)

print(f"Expanded SOC codes: {len(expanded_soc)}")

# Helper function to prune datasets
def prune_dataset(filename, key_soc_field="onetsoc_code"):
    with open(RAW_DIR / filename, "r", encoding="utf-8") as f:
        data = json.load(f)["row"]  # <-- all O*NET JSON tables store rows under "row"

    pruned = [
        row for row in data
        if row.get(key_soc_field) in expanded_soc
    ]

    out_file = OUT_DIR / f"{filename.replace('.json', '')}_pruned.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(pruned, f, indent=2)

    print(f"Pruned {filename}: {len(pruned)} rows → {out_file}")

# Step 2: Prune each dataset
prune_dataset("software_skills.json")
prune_dataset("essential_skills.json")
prune_dataset("transferable_skills.json")
prune_dataset("knowledge.json")

print("Pruning complete.")
