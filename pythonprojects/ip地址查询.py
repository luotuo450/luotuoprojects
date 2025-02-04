import requests


def get_ip_location(ip):
    """
    根据给定的 IP 地址获取其现实世界中的地理位置
    :param ip: 要查询的 IP 地址
    :return: 包含地理位置信息的字符串，如果查询失败则返回 None
    """
    try:
        # 构建请求的 URL
        url = f"https://ipapi.co/{ip}/json/"
        # 发送 GET 请求
        response = requests.get(url)
        # 检查响应状态码是否为 200（表示请求成功）
        if response.status_code == 200:
            # 将响应内容解析为 JSON 格式
            data = response.json()
            # 提取城市、地区和国家名称信息
            city = data.get("city", "未知城市")
            region = data.get("region", "未知地区")
            country = data.get("country_name", "未知国家")
            # 组合地理位置信息
            location = f"{city}, {region}, {country}"
            return location
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except requests.RequestException as e:
        print(f"发生网络请求错误: {e}")
    return None


# 示例使用
if __name__ == "__main__":
    ip_address = input("请输入要查询的 IP 地址: ")  # 替换为你要查询的 IP 地址
    location = get_ip_location(ip_address)
    if location:
        print(f"IP {ip_address} 对应的现实世界地址是: {location}")
    else:
        print(f"无法获取 IP {ip_address} 的地理位置信息。")
