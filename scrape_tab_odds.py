import requests
import json
from bs4 import BeautifulSoup

def scrape_tab_odds():
    url = "https://www.tab.co.nz/sports/basketball/new-zealand/nz-nbl"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("❌ 获取TAB页面失败")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    # 示例抓取逻辑：模拟结构
    # 实际应定位比赛项与盘口项，目前为演示结构（你可根据TAB实际结构修改）

    matches = soup.find_all("div", class_="event-row")[:5]  # 假设类名为 event-row
    for match in matches:
        try:
            teams = match.find("div", class_="teams").text.strip()
            total_points_line = 182.5  # 需要从页面中解析出来
            odds = 1.85  # 同样从页面中提取

            results.append({
                "match": teams,
                "market": "Total Points",
                "line": total_points_line,
                "odds": odds
            })
        except:
            continue

    with open("data/tab_odds.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"✅ 成功写入 {len(results)} 条盘口数据到 data/tab_odds.json")

if __name__ == "__main__":
    scrape_tab_odds()
