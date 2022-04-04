# statink_scraper
Stat.inkに格納されたSplatoon2の成績をエクセル上で管理するためのスクレインピングツール  

# 必要なもの
- stat.inkアカウントと戦績データ  
- Python実行環境  
- Excel  

# 処理の流れ
- stat.inkの月報を Python で自動取得  
![image](https://user-images.githubusercontent.com/102900238/161623696-8a76cd84-daee-44c1-b616-443f66638f24.png)
- Python でスクレイピングし、tab区切りの表として出力  
![image](https://user-images.githubusercontent.com/102900238/161624104-5db94d78-f1b1-4a13-89e4-15733d69d767.png)
- [手動] エクセルにコピー＆ペーストで貼り付ける  
- ![image](https://user-images.githubusercontent.com/102900238/161624740-bede0cab-06cd-4802-a90c-15e59391021a.png)
- [手動] "マクロ"シートのボタンを押すことで、ステージ名ソートや勝率順ソート、成績を追加入力するための列の挿入が可能
- [手動] 今月のステージの選定は手入力で行う
- [手動] 今月のステージの良し悪しをじっくり検討する
![image](https://user-images.githubusercontent.com/102900238/161626619-4456c625-7a76-402d-83f8-20fc1e9630aa.png)
