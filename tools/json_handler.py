import json
from pathlib import Path
from typing import Union

from config.path_conf import api_docs_path
from tools.logger import Logger

logger = Logger().get_logger()


def load_case_from_json(filename: Union[str, Path]) -> dict:
    logger.info("从 json 文件中读取用例数据")
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def dump_case_to_json(cases_str: str, filename: Union[str, Path]) -> None:
    logger.info("将用例写入 json 文件")
    with open(filename, "w", encoding="utf-8") as json_file:
        cases = json.loads(cases_str)
        json.dump(cases, json_file, indent=4, ensure_ascii=False)


def load_prompt_from_md(filename: Union[str, Path]) -> str:
    logger.info("从 md 文档中读取提示词")
    with open(filename, "r", encoding="utf-8") as md:
        prompt = md.read()
    return prompt


def load_from_api_doc(filename: Union[str, Path]) -> str:
    logger.info("从 api 文档中读取接口结构定义")
    with open(filename, "r", encoding="utf-8") as api_doc:
        api_doc_str = api_doc.read()
    return api_doc_str


def dump_user_upload_api_doc(api_doc_str: str) -> None:
    """将用户上传的 api 文档读取之后写入到新的 json 文件中"""
    with open(api_docs_path, "w", encoding="utf-8") as api_doc:
        api_doc.write(api_doc_str)
