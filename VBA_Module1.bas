Attribute VB_Name = "Module1"
'入力済みセルの右端を出力
Function column_end(ByVal she As String) As String
    Sheets(she).Select
    i = 1
    While Cells(2, i).Value <> ""
        i = i + 1
    Wend
    'MsgBox Cells(2, i - 1)
    column_end = i - 1
End Function

'月次成績を入力するための列を追加
Function func_insert_column(ByVal she As String)
    Sheets(she).Select
    Columns("D:E").Select
    Selection.Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromRightOrBelow
    Sheets(she).Range("D2").Value = "通算成績" + vbCrLf + Str(Date)
    Sheets(she).Range("E2").Value = "単月" + vbCrLf + Str(Month(Now) - 1) + "月末"
    Sheets(she).Range("D26").Value = "=COUNT(D3:D25)"
    Sheets(she).Range("E26").Value = "=COUNT(E3:E25)"
End Function

'ソート
Function func_sort(ByVal she As String, ByVal key As String, ByVal ord As String)
    en = column_end(she)
    Sheets(she).Select
    ActiveWorkbook.Worksheets(she).AutoFilter.sort.SortFields.Clear
    If ord = "As" Then
        ActiveWorkbook.Worksheets(she).AutoFilter.sort.SortFields.Add2 key:= _
            Range(key + "2:" + key + en), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
    ElseIf ord = "Des" Then
        ActiveWorkbook.Worksheets(she).AutoFilter.sort.SortFields.Add2 key:= _
            Range(key + "2:" + key + en), SortOn:=xlSortOnValues, Order:=xlDescending, DataOption:=xlSortNormal
    Else
       Exit Function
    End If
       
    With ActiveWorkbook.Worksheets(she).AutoFilter.sort
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With

End Function

'月次成績を入力するための列を追加
Sub Insert_columns()
    Call func_insert_column("1_エリア勝率")
    Call func_insert_column("3_ヤグラ勝率")
    Call func_insert_column("2_ホコ勝率")
    Call func_insert_column("4_アサリ勝率")
    Sheets("macro").Select
End Sub

'ステージ名（アルファベット）でフィルターを昇順ソート
Sub sort_stage()
    Call func_sort("1_エリア勝率", "A", "As")
    Call func_sort("3_ヤグラ勝率", "A", "As")
    Call func_sort("2_ホコ勝率", "A", "As")
    Call func_sort("4_アサリ勝率", "A", "As")
    Sheets("macro").Select
End Sub

'成績でフィルターを降順ソート
Sub sort_stats()
    Call func_sort("1_エリア勝率", "D", "Des")
    Call func_sort("3_ヤグラ勝率", "D", "Des")
    Call func_sort("2_ホコ勝率", "D", "Des")
    Call func_sort("4_アサリ勝率", "D", "Des")
    Sheets("macro").Select
End Sub

