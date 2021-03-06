# TEXT CONVERT UNICODE
---
_Function to convert unicode text._

|_args_| _type_ | description |
|------|--------|-------------|
| text | str | text convert, to defaults |
| show | bool| show details, to defaults false
| reverse | bool | show details reverse, to defaults false

_Return List_ 
~~~ python
[{'ascii_list': [112, 121, 116, 104, 111, 110], 'char_list': ['p', 'y', 't', 'h', 'o', 'n'], 'binary_list': ['1110000', '1111001', '1110100', '1101000', '1101111', '1101110'], 'hex_list': ['70', '79', '74', '68', '6F', '6E']}]
~~~

_consult table_ [ASCII](https://pt.wikipedia.org/wiki/ASCII)

_example_

~~~python
from text_convert_unicode import *

tcu('python', show=True)
~~~
_result_

~~~cmd
------------------------------------------------------------------------------------------
                                   TEXT CONVERT UNICODE
------------------------------------------------------------------------------------------
     CHARACTER              ASCII                 HEX                 BINARY

         p                   112                   70                1110000       
         y                   121                   79                1111001
         t                   116                   74                1110100
         h                   104                   68                1101000
         o                   111                   6F                1101111
         n                   110                   6E                1101110
------------------------------------------------------------------------------------------
python ==> 111000011110011110100110100011011111101110
------------------------------------------------------------------------------------------
~~~
_reverse_
~~~python
from text_convert_unicode import *

tcu('python', show=True, reverse=True)
~~~
~~~cmd
------------------------------------------------------------------------------------------
                                   TEXT CONVERT UNICODE
------------------------------------------------------------------------------------------
       BINARY               ASCII                 HEX               CHARACTER

      1110000                112                   70                   p
      1111001                121                   79                   y
      1110100                116                   74                   t
      1101000                104                   68                   h
      1101111                111                   6F                   o
      1101110                110                   6E                   n
------------------------------------------------------------------------------------------
111000011110011110100110100011011111101110 ==> python
------------------------------------------------------------------------------------------
~~~

__install__
~~~~ shell
pip install text-convert-unicode
~~~~