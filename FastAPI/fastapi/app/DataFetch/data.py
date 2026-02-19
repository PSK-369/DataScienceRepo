import json
from pathlib import Path
from typing import List, Dict


DATA_FILE = Path(__file__).parent.parent / "data" / "sample.json"


def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    else:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)


def get_allproducts() -> List[Dict]:
    return load_products()
