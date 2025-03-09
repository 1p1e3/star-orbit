import pytest
import requests

from config.path_conf import cases_json_path
from tools.json_handler import load_case_from_json

cases_dict: dict = load_case_from_json(cases_json_path.as_posix())

@pytest.mark.parametrize("case", cases_dict, ids=[case_id for case_id in cases_dict.keys() ])
def test_build(case):

    res = requests.request(
        method=cases_dict[case].get("method"),
        url=cases_dict[case].get("url"),
        headers=cases_dict[case].get("headers"),
        params=None if not cases_dict[case].get("params") else cases_dict[case].get("params"),
        json=None if not cases_dict[case].get("body") else cases_dict[case].get("body"),
    )
    # 断言
    assert res.status_code == cases_dict[case].get("expectedStatusCode")
    assert res.json() == cases_dict[case].get("expectedFields")