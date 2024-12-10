### Cell
    $A$2: fixed column and row
    A$2: fixed row
    $A2: fixed column

#### Custom number format
    0: display zeros
    (use #.00 > 9.20)

### Omit extra zeros displayed 
    (use #.## > 3.4)

### Keyboard short cuts
    ctrl A > select entire table 
    ctrl Z > undo
    ctrl; > fixed date 
    ctrl shift; > fixed time
    = today() > current date
    = now() > current date and time

### Database function
    1. Build criteria range (same row = AND, different rows = OR)
    2. Cell > DSUM or DAVERAGE > specify database > specify column > specify criteria > ok

### Formulas symbols
    greater than >
    greater than or equal to >=
    less than <
    less than or equal to <=
    not equal to/except <>
    equal to =

<br/>

### Advanced filter
    1. Build criteria range (same row = AND, different rows = OR)
    2. Place cell pointer to database > Data ribbon > specify criteria > Tick copy to > specify copy to location > ok

### Advanced filter and database function > must build criteria range
    1. Must include header in selection for database and criteria
    2. Same row = AND
    3. Different rows = OR

### PivotTable fields
    1. Filters: level
    2. Columns: divison
    3. Rows: gender
    4. Values: sum of salary

### VLOOKUP
    =VLOOKUP(lookup value, range containing the lookup value, the column number in the range containing the return value, approximate match (TRUE) or exact match (FALSE))

<br/>

## VBA
### vba button chart

    Private Sub CommandButton1_Click()
    Range("A1:A5,B1:B5").Select
    ActiveSheet.Shapes.AddChart.Select
    ActiveChart.SetSourceData Source:=Range("'vba chart button'!$A$1:$A$5,'vba chart button'!$B$1:$B$5")
    ActiveChart.ChartType = xlColumnClustered
    ActiveSheet.ChartObjects(1).Activate
    Sheets("vba chart button").Select
    End Sub

### Automate chart creation using Excel macros

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

<br/>