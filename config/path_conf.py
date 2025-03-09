import pathlib

# 根目录
root_path = pathlib.Path(__file__).parent.parent

# core 目录
core_path = root_path.joinpath('core')

# prompts 目录
prompts_path = root_path.joinpath('prompts')

# 用于生成用例的提示词路径
case_generate_prompt_path = prompts_path.joinpath('case_generate.md')

# case
cases_json_path = root_path.joinpath('cases', 'cases.json')

# api 接口文档目录
api_docs_path = root_path.joinpath('api_docs', "api_doc.json")

# 测试报告和结果输出目录
output_path = root_path.joinpath('output')

