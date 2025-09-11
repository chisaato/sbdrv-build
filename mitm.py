from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    """
    拦截指定URL的请求并返回固定响应
    """
    # 检查请求的URL是否匹配目标地址
    if flow.request.pretty_url.startswith("https://sandboxie-plus.com/get_cert.php"):
        # 构造固定响应
        fixed_response_text = """
NAME: 114514
LEVEL: ETERNAL
DATE: 05.07.2099
UPDATEKEY: xxxxx
SIGNATURE: xxxx
"""

        # 返回固定文本响应
        flow.response = http.Response.make(
            200,  # HTTP状态码
            fixed_response_text.encode("utf-8"),  # 响应体内容
            {"Content-Type": "text/plain"},  # 响应头
        )
