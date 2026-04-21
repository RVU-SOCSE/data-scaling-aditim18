Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/laptop.py
Traceback (most recent call last):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/laptop.py", line 2, in <module>
    df = pd.read_csv('4laptops.csv')
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 306, in _read
    return parser.read(nrows)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1947, in read
    ) = self._engine.read(  # type: ignore[attr-defined]
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 215, in read
    chunks = self._reader.read_low_memory(nrows)
  File "pandas/_libs/parsers.pyx", line 832, in pandas._libs.parsers.TextReader.read_low_memory
  File "pandas/_libs/parsers.pyx", line 897, in pandas._libs.parsers.TextReader._read_rows
  File "pandas/_libs/parsers.pyx", line 868, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 885, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2084, in pandas._libs.parsers.raise_parser_error
pandas.errors.ParserError: Error tokenizing data. C error: Expected 2214 fields in line 3, saw 6203


= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/laptop.py
Traceback (most recent call last):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/laptop.py", line 4, in <module>
    df = pd.read_csv('4laptops.csv')
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 306, in _read
    return parser.read(nrows)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1947, in read
    ) = self._engine.read(  # type: ignore[attr-defined]
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 215, in read
    chunks = self._reader.read_low_memory(nrows)
  File "pandas/_libs/parsers.pyx", line 832, in pandas._libs.parsers.TextReader.read_low_memory
  File "pandas/_libs/parsers.pyx", line 897, in pandas._libs.parsers.TextReader._read_rows
  File "pandas/_libs/parsers.pyx", line 868, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 885, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2084, in pandas._libs.parsers.raise_parser_error
pandas.errors.ParserError: Error tokenizing data. C error: Expected 2214 fields in line 3, saw 6203


= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/laptop.py
Traceback (most recent call last):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/laptop.py", line 2, in <module>
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
ModuleNotFoundError: No module named 'sklearn'

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/laptop.py
After One Hot Encoding:
      TypeName   RAM  ...  TypeName_Ultrabook  TypeName_Workstation
0    Ultrabook   8GB  ...                 1.0                   0.0
1     Notebook  16GB  ...                 0.0                   0.0
2       Gaming   8GB  ...                 0.0                   0.0
3     Notebook   4GB  ...                 0.0                   0.0
4  Workstation  32GB  ...                 0.0                   1.0

[5 rows x 6 columns]

After Label Encoding RAM:
      TypeName  RAM  ...  TypeName_Ultrabook  TypeName_Workstation
0    Ultrabook    3  ...                 1.0                   0.0
1     Notebook    0  ...                 0.0                   0.0
2       Gaming    3  ...                 0.0                   0.0
3     Notebook    2  ...                 0.0                   0.0
4  Workstation    1  ...                 0.0                   1.0

[5 rows x 6 columns]

RAM Classes:
['16GB' '32GB' '4GB' '8GB']

==================== RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/prog11/salaryyy.py ====================
Traceback (most recent call last):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/prog11/salaryyy.py", line 5, in <module>
    df = pd.read_csv('11prog_3Salary_Data.csv')
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '11prog_3Salary_Data.csv'

==================== RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/prog11/salaryyy.py ====================
Original Dataset:
   YearsExperience  Salary
0              1.1   39343
1              1.3   46205
2              1.5   37731
3              2.0   43525
4              2.2   39891

Numerical Data:
   YearsExperience  Salary
0              1.1   39343
1              1.3   46205
2              1.5   37731
3              2.0   43525
4              2.2   39891

Standard Scaled Data:
   YearsExperience    Salary
0        -1.510053 -1.360113
1        -1.438373 -1.105527
2        -1.366693 -1.419919
3        -1.187494 -1.204957
4        -1.115814 -1.339781

Min-Max Scaled Data:
   YearsExperience    Salary
0         0.000000  0.019041
1         0.021277  0.100094
2         0.042553  0.000000
3         0.095745  0.068438
4         0.117021  0.025514

Normalized Data:
   YearsExperience  Salary
0         0.000028     1.0
1         0.000028     1.0
2         0.000040     1.0
3         0.000046     1.0
4         0.000055     1.0

=================== RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/prog12/salaryyyy1.py ===================
Traceback (most recent call last):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/prog12/salaryyyy1.py", line 3, in <module>
    df2 = pd.read_csv("4laptops.csv")
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 306, in _read
    return parser.read(nrows)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1947, in read
    ) = self._engine.read(  # type: ignore[attr-defined]
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 215, in read
    chunks = self._reader.read_low_memory(nrows)
  File "pandas/_libs/parsers.pyx", line 832, in pandas._libs.parsers.TextReader.read_low_memory
  File "pandas/_libs/parsers.pyx", line 897, in pandas._libs.parsers.TextReader._read_rows
  File "pandas/_libs/parsers.pyx", line 868, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 885, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2084, in pandas._libs.parsers.raise_parser_error
pandas.errors.ParserError: Error tokenizing data. C error: Expected 2214 fields in line 3, saw 6203

>>> 
=================== RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab14/prog12/salaryyyy1.py ===================
Dataset Info:
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Columns: 2214 entries, <!DOCTYPE html><html dir="ltr"><head><script nonce="XBAH3gNZDDq_s0fU52XZJg"> window['_DRIVE_VIEWER_ctiming']={}; </script><meta name="google" content="notranslate"><meta http-equiv="X-UA-Compatible" content="IE=edge;"><style nonce="Tm2aNBZAtO3eQwBuQPPtvQ">@font-face{font-family:'Roboto';font-style:italic;font-weight:400;font-stretch:100%;src:url(//fonts.gstatic.com/s/roboto/v48/KFOKCnqEu92Fr1Mu53ZEC9_Vu3r1gIhOszmOClHrs6ljXfMMLoHQuAX-lXYi128m0kN2.woff)format('woff');unicode-range:U+0460-052F to U+FFFD;}</style><meta name="referrer" content="origin"><title>10prog_4laptops.csv - Google Drive</title><script nonce="XBAH3gNZDDq_s0fU52XZJg">
dtypes: float64(2213), str(1)
memory usage: 17.4 KB
None

Matplotlib Box Plots (Column-wise):
clear
