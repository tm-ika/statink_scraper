Attribute VB_Name = "Module1"
'���͍ς݃Z���̉E�[���o��
Function column_end(ByVal she As String) As String
    Sheets(she).Select
    i = 1
    While Cells(2, i).Value <> ""
        i = i + 1
    Wend
    'MsgBox Cells(2, i - 1)
    column_end = i - 1
End Function

'�������т���͂��邽�߂̗��ǉ�
Function func_insert_column(ByVal she As String)
    Sheets(she).Select
    Columns("D:E").Select
    Selection.Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromRightOrBelow
    Sheets(she).Range("D2").Value = "�ʎZ����" + vbCrLf + Str(Date)
    Sheets(she).Range("E2").Value = "�P��" + vbCrLf + Str(Month(Now) - 1) + "����"
    Sheets(she).Range("D26").Value = "=COUNT(D3:D25)"
    Sheets(she).Range("E26").Value = "=COUNT(E3:E25)"
End Function

'�\�[�g
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

'�������т���͂��邽�߂̗��ǉ�
Sub Insert_columns()
    Call func_insert_column("1_�G���A����")
    Call func_insert_column("3_���O������")
    Call func_insert_column("2_�z�R����")
    Call func_insert_column("4_�A�T������")
    Sheets("macro").Select
End Sub

'�X�e�[�W���i�A���t�@�x�b�g�j�Ńt�B���^�[�������\�[�g
Sub sort_stage()
    Call func_sort("1_�G���A����", "A", "As")
    Call func_sort("3_���O������", "A", "As")
    Call func_sort("2_�z�R����", "A", "As")
    Call func_sort("4_�A�T������", "A", "As")
    Sheets("macro").Select
End Sub

'���тŃt�B���^�[���~���\�[�g
Sub sort_stats()
    Call func_sort("1_�G���A����", "D", "Des")
    Call func_sort("3_���O������", "D", "Des")
    Call func_sort("2_�z�R����", "D", "Des")
    Call func_sort("4_�A�T������", "D", "Des")
    Sheets("macro").Select
End Sub

