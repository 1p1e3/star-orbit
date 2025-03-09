import pathlib

# 根目录
root_path = pathlib.Path(__file__).parent.parent

# core 目录
core_path = root_path.joinpath('core')

# prompts 目录
prompts_path = root_path.joinpath('prompts')

case_generate_prompt_path = prompts_path.joinpath('case_generate.md')

# case
cases_json_path = root_path.joinpath('output.json')

