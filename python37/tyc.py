"""基于asyncio的天眼查接口"""

import asyncio
import aiohttp
import json

BASE_URL = "http://open.api.tianyancha.com/services/v4/open/"
HEADERS = {"Authorization": "T30uTDkfNbDI"}

URL_MAP = {
    "base_info": "baseinfo",   # 基本信息
    "partner": "holder",    # 股东信息
    "annual_report": "annualreport",  # 企业年报
    "reg_works": "copyRegWorks",  # 作品著作权
    "copy_reg": "copyReg",  # 著作权
    "patents": "patents",  # 专利
    "find_history_rongzi": "findHistoryRongzi",   # 融资历史
    "certificate": "certificate",   # 证书
    "tax_credit": "taxCredit",  # 税务评级
    "employments": "employments",  # 招聘
}

BASE_INFO = ["categoryScore", "percentileScore", "regCapital", "tags",
             "regStatus", "toTime"]

parter = ["total", "toco", "capitalActl", "capital"]

annual_report = ["reportYear", "companyName", "manageState", "employeeNum",
                 "operatorName", "totalAssets", "totalEquity", "totalSales",
                 "totalProfit", "primeBusProfit", "retainedProfit", "totalTax",
                 "totalLiability", "investorName", "subscribeAmount",
                 "subscribeTime", "subscribeType", "paidAmount", "paidTime",
                 "paidTime", "paidType"]

find_history_rongzi = ["date", "investorName", "money", "round", "share",
                       "value"]

certificate = ["total", "certificateName", "startDate", "endDate"]

tax_credit = ["grade", "year", "eval", "evalDepartment", "type"]

employments = ["total", "title", "createTime", "employerNumber", "enddate"]

field_map = {
    "base_info": BASE_INFO, "partner": parter, "annual_report": annual_report,
    "find_history_rongzi": find_history_rongzi, "certificate": certificate,
    "tax_credit": tax_credit, "employments": employments, }

total_list = ["reg_works", "copy_reg", "patents"]


@asyncio.coroutine
async def getInfo(url, keys, company_name, result_dict):
    """获取信息"""
    url = BASE_URL + url + "?name=" + company_name
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as resp:
            text = await resp.text()
            # assert text["error_code"] == 0
            result_dict[keys] = json.loads(text)


def tyc_info(company_name):
    """总的信息汇总"""
    loop = asyncio.get_event_loop()
    res = {}
    tasks = [getInfo(url, keys, company_name, res) for keys, url in
             URL_MAP.items()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    return res


def handle_result(result):
    """处理异步获取到的结果"""
    result_dic = {}
    # 处理需要返回详细字段的内容
    for k, keys in field_map.items():
        k_result = result.get(k, None)
        if k_result and k_result["error_code"] == 0:
            k_result = k_result["result"]
            print(k_result)
            for key in keys:
                vals = k_result.get(key, "")
                if key == "total":
                    key = k + "_" + "total"
                result_dic[key] = vals
        else:
            for key in keys:
                if key == "total":
                    key = k + "-" + "total"
                result_dic[key] = "-"
    # 处理需要返回total的内容
    for key in total_list:
        k_result = result.get(key, None)
        key = key + "_" + "total"
        if k_result and k_result["error_code"] == 0:
            k_result = k_result["result"]
            result_dic[key] = k_result["total"]
        else:
            result_dic[key] = "-"
    return result_dic


if __name__ == "__main__":
    result = tyc_info("北京百度网讯科技有限公司")
    print(result)
    re = json.dumps(result)
    with open("tyc.txt", "w") as f:
        f.write(re)
