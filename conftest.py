import datetime
import pytest
from tools.logger import Logger

log_obj = Logger()

def pytest_runtest_makereport(item, call):
    report = pytest.TestReport.from_item_and_call(item, call)
    report.description = getattr(item, "description", "No description available")
    return report

def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")

def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")

def pytest_configure(config):

    """设置测试报告文件名称和保存路径"""

    report_name = f"report-{log_obj.get_the_datetime_of_the_log_name()}.html"
    report_path = log_obj.get_current_round_log_storage_path().joinpath(report_name)
    config.option.htmlpath = report_path
