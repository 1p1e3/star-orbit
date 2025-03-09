from google import genai
from config.path_conf import case_generate_prompt_path, api_docs_path, cases_json_path
from tools.json_handler import dump_case_to_json, load_prompt_from_md, load_from_api_doc
from tools.logger import Logger

logger = Logger().get_logger()


def gemini_client():
    # 创建客户端
    client = genai.Client(api_key="your_api_key")

    # 创建对话
    chat = client.chats.create(model="gemini-2.0-flash")


    prompt = load_prompt_from_md(case_generate_prompt_path)

    # 初始化角色
    role_set = chat.send_message(message=prompt)

    logger.info(f"Gmini输出:{role_set.text}")

    # 读取 api 文档数据
    api_doc = load_from_api_doc(api_docs_path)

    # 处理 api 文档，生成用例
    api_doc_handle = chat.send_message(message=api_doc)

    logger.info("Gemini 开始生成用例")

    # 提取JSON结果
    cases_json_data = api_doc_handle.candidates[0].content.parts[0].text.strip("```").strip("json")

    print("用例数据", cases_json_data)

    # 写入文件
    dump_case_to_json(cases_json_data, cases_json_path)

    logger.info("Gemini 用例生成结束")

