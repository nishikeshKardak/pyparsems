pyparsems
==========

Parses a long millisecond value as a dict object.

## Install

```
pip install pyparsems
```

or

```
python setup.py install
```

## Usage

```
from pyparsems import parseMillSecs

parseMilliSecs().parse_millisecs(1545068932)

# output
{
	days: 17,
	hours: 21,
	minutes: 11,
	seconds: 9,
	milliseconds: 931 ,
	microseconds: 68,
	nanoseconds: 545
}

```
