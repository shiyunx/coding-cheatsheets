## vba button chart

    Private Sub CommandButton1_Click()

    Range("A1:A5,B1:B5").Select
    ActiveSheet.Shapes.AddChart.Select
    ActiveChart.SetSourceData Source:=Range("'vba chart button'!$A$1:$A$5,'vba chart button'!$B$1:$B$5")
    ActiveChart.ChartType = xlColumnClustered
    ActiveSheet.ChartObjects(1).Activate
    Sheets("vba chart button").Select
    
    End Sub


## Automate chart creation using Excel macros

    Private Sub CommandButton1_Click()

    Range("A1:A5,B1:B5").Select
    ActiveSheet.Shapes.AddChart.Select
    ActiveChart.SetSourceData Source:=Range("'vba chart button'!$A$1:$A$5,'vba chart button'!$B$1:$B$5")
    ActiveChart.ChartType = xlColumnClustered
    ActiveSheet.ChartObjects(1).Activate
    ActiveSheet.ChartObjects(1).Cut
    Sheets("Sheet2").Select
    ActiveSheet.Paste
    Sheets("vba chart button").Select
    Range("F9").Activate

    End Sub