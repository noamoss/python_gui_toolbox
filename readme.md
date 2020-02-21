## Common Python GUI tools

### Usage:
1. Clone the repo.
2. find the relevant gui tool (i.e. `IntputOutputPath`)
3. Import `IntputOutputPath` from pythonGUI.


### InputOutputPath
* usage:
```
from ui import InputoutputPath
file_path = IntputOutputPath(parameters)`
```
A default window will pop-up, asking user to type in or browse for input and output files path.

type or call `file_path.inputfile` or `file_path.outputfil` to get the chose file(s) path.

Parameters:
-`window_title`: text to be displayed at the top of the window. Default: `Please choose file(s) path`
- `dir`: (`ltr`/`rtl`) the gui orientation. Deafult: `ltr` (English)
- `types`: (`[input, output]` / `input`/`output`/) What types of file(s) path to ask for, Default:`[intput, output`]

- `label1`: text to be displayed as the input file path label. Default: `Choose input file path:` (for LTR) / `בחר/י מיקום קובץ קלט:` (for RTL)
- `button1`: text to be displayed on the inputfile browse button. Deafult: `Browse` (for LTR) / `בחר/י` (for RTL)
- `label2` : text to be displayed as the output file path label. Default: `Choose output file path:` (for LTR) / `בחר/י מיקום קובץ פלט:` (for RTL)
- `button2`: text to be displayed on the outputfile browse button. Default: `Browse` (for LTR) / `בחר/י` (for RTL)
- `button_submit`: text to be displayed on the Submit button. Default: `Submit` (for LTR) / `אישור` (for RTL)

