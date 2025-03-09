from core.agent import gemini_client
import pytest
import argparse
from tools.json_handler import load_from_api_doc, dump_user_upload_api_doc
from tools.logger import Logger
logger = Logger().get_logger()

def main():
    parser = argparse.ArgumentParser(description="StarOrbit CLI 工具")
    parser.add_argument("--doc", type=str, help="接口文档路径(json格式, 绝对路径)")

    args = parser.parse_args()

    if args.doc is not None:
        try:
            data = load_from_api_doc(args.doc)
            dump_user_upload_api_doc(data)
        except Exception as e:
            logger.error(f"接口文档数据读取失败,请检查接口文档路径(必须是绝对路径)是否错误,或接口文档不符合 json 格式规范:{e}")
            exit(1)

    gemini_client()
    pytest.main(["-s"])


if __name__ == '__main__':
    main()