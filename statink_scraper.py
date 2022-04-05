#!/usr/bin/python
# -*- coding: <encoding utf-8> -*-

import requests
from bs4 import BeautifulSoup


# stat.inkアカウント ログインは不要
my_account = "@YOUR_STATINK_ACCOUNT"


def check_win_rate(result, div, rule):
    print(rule)
    if '<div class="text-muted">No Data</div>' in str(div):
        print("*** No-data ***")
    sub_divs = div.find_all("div" ,class_='row mb-2')
    for sub_div in sub_divs:
        val = sub_div.find("div" ,class_='pie-chart win-pct')
        img = sub_div.find_all("img" ,class_='auto-tooltip w-100')

        val = str(val).split("data-values='{")[-1]
        win = val.split(",")[0].split(":")[-1]
        lose= val.split("}")[0].split(":")[-1]
        win_rate = round(float(win)*100/(float(win)+float(lose)),1)
        stage = str(img).split(".jpg")[0].split("/")[-1]
        result[rule][stage] = win_rate


# 戦績を格納するためのリスト
result = {"area":"","yagura":"","hoko":"","asari":""}
result["area"]={"ajifry":"-","ama":"-","anchovy":"-","arowana":"-","battera":"-","bbass":"-","chozame":"-","devon":"-","engawa":"-","fujitsubo":"-","gangaze":"-","hakofugu":"-","hokke":"-","kombu":"-","manta":"-","mongara":"-","mozuku":"-","mutsugoro":"-","otoro":"-","shottsuru":"-","sumeshi":"-","tachiuo":"-","zatou":"-"}
result["yagura"]={"ajifry":"-","ama":"-","anchovy":"-","arowana":"-","battera":"-","bbass":"-","chozame":"-","devon":"-","engawa":"-","fujitsubo":"-","gangaze":"-","hakofugu":"-","hokke":"-","kombu":"-","manta":"-","mongara":"-","mozuku":"-","mutsugoro":"-","otoro":"-","shottsuru":"-","sumeshi":"-","tachiuo":"-","zatou":"-"}
result["hoko"]={"ajifry":"-","ama":"-","anchovy":"-","arowana":"-","battera":"-","bbass":"-","chozame":"-","devon":"-","engawa":"-","fujitsubo":"-","gangaze":"-","hakofugu":"-","hokke":"-","kombu":"-","manta":"-","mongara":"-","mozuku":"-","mutsugoro":"-","otoro":"-","shottsuru":"-","sumeshi":"-","tachiuo":"-","zatou":"-"}
result["asari"]={"ajifry":"-","ama":"-","anchovy":"-","arowana":"-","battera":"-","bbass":"-","chozame":"-","devon":"-","engawa":"-","fujitsubo":"-","gangaze":"-","hakofugu":"-","hokke":"-","kombu":"-","manta":"-","mongara":"-","mozuku":"-","mutsugoro":"-","otoro":"-","shottsuru":"-","sumeshi":"-","tachiuo":"-","zatou":"-"}


m = str(int(input("[?] 何月の戦績が必要?：")))
query = "/spl2/stat/monthly-report/2022/" + m
url = "https://stat.ink/" + my_account + query

print("*************")
print("[>] 指定月の戦績の出力(勝率%)")
print("[>] HTTPreq to stat.ink...")
print(url)
res = requests.get(url)
res_text=res.text

# splitでスクレイピング範囲をガチマッチに絞る
res_text=res_text.split('<h2 id="league4">')[0]
res_text=res_text.split('<h2 id="league2">')[0]
res_text=res_text.split('<h2 id="gachi">')[-1]

# スクレイピング
soup = BeautifulSoup(res_text, "html.parser")
divs = soup.find_all("div" ,class_='col-12 col-md-6 col-lg-3 mb-3')
for div in divs:
    if '<h3 class="mt-0">Splat Zones</h3>' in str(div):
        rule = "area"
        check_win_rate(result,div,rule)
    elif '<h3 class="mt-0">Tower Control</h3>' in str(div):
        rule = "yagura"
        check_win_rate(result,div,rule)
    elif '<h3 class="mt-0">Rainmaker</h3>' in str(div):
        rule = "hoko"
        check_win_rate(result,div,rule)
    elif '<h3 class="mt-0">Clam Blitz</h3>' in str(div):
        rule = "asari"
        check_win_rate(result,div,rule)

# ヘッダの出力
print("\t", "area", "\t", "yagura", "\t", "hoko", "\t", "asari")
for k in result["area"].keys():
    print(k, "\t", result["area"][k], "\t", result["yagura"][k], "\t", result["hoko"][k], "\t", result["asari"][k])
	
print("*************")

# 通算成績
query = "/spl2/stat/by-map-rule?filter%5Brule%5D=standard-gachi-any"
url = "https://stat.ink/" + my_account + query

print("[>] 通算成績の出力(勝率%)　※ガチマだけでなく２リグ、４リグ、プラベの成績を含む")
print("[>] HTTPreq to stat.ink...")
print(url)

# スクレイピング
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
divs = soup.find_all("div" ,class_='pie-flot-container')

stage_org = ""
all_result = []
part_result = []


for div in divs[5:]:
   
    result_list = str(div).split("%5D=")
    rule = result_list[1].split("&amp;")[0].split("-")[-1]

    stage = result_list[2].split("data-json=")[0].replace('"',"").strip()
    j_str = (result_list[2].split("data-json=")[1]).split(">")[0]
    result_list = j_str.split(",")

    win = int(result_list[0].split(":")[1])
    lose = int(result_list[1].split(":")[1])

    # ミステリーゾーンは省く
    if not stage.startswith("mystery"):

        if not(stage ==  stage_org):
            if len(part_result) > 0:
                all_result.append(part_result)
            part_result = [stage]
            # 極端に試合数が少ない戦績は省く
            if win + lose < 4:
                result = "-"
                part_result.append(rule+" "+str(result))
            else:
                result = round(win * 100 / (win + lose))
                part_result.append(rule+" "+str(result))
        elif stage ==  stage_org:
            # 極端に試合数が少ない戦績は省く
            if win + lose < 4:
                result = "-"
                part_result.append(rule+" "+str(result))
            else:
                result = round(win * 100 / (win + lose))
                part_result.append(rule+" "+str(result))

    stage_org = stage


all_result.append(part_result)    

for i in sorted(all_result):
    for a in i:
        a=a.replace(" ", "\t")
        print(a,end ="\t")
    print("")

print(len(all_result))
if len(all_result) < 23:
    for result in all_result:
        print(result[0])


input("end...")
