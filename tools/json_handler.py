import json
from pathlib import Path
from typing import Union


def load_case_from_json(filename: Union[str, Path]) -> dict:
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def dump_case_to_json(cases_str: str, filename: Union[str, Path]) -> None:
    with open(filename, "w", encoding="utf-8") as json_file:
        cases = json.loads(cases_str)
        json.dump(cases, json_file, indent=4, ensure_ascii=False)
