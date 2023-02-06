
This little script converts and reconverts text (in UTF-8 encoding) into binary data representated as TAB(0) and SPACE(1) for maximal readability, ease of use and most importantly space efficiency - because nothing is as efficient as an 8x increase in space requirements.

# Context

This is partially inspired by the paradigm-shifting [Whitespace programming language](https://en.wikipedia.org/wiki/Whitespace_(programming_language)), a language using only SPACE, TAB, and LINEBREAK to convey logic, but using three different characters (and allowing more unused ones) seems to be a bit overkill and could significantly impact readability, therefore a generalized solution that can also encode common **Whitespace** programs with only tabs and spaces was desperately needed.
As an example, I have [encoded](examples/whitespace_encoded) a [whitespace "Hello World!" example](examples/whitespace) to really highlight what this wonderful script can do! I think we can all agree that it looks much better now.

# Example

```
'Hello World'
```

is encoded so give us the much more useful following string:

#
```
'
	 		 				  		 	 	  	  			  	  			  	    		 						 	 	   	  	    	   		 		  	  			  		 		'
```

and yes, we can obviously revert this encoding back to give us 

```
'Hello World'
```

again.

# Usage

## Example

```python
python3 main.py main.py encoded --encode
```
encodes the *main.py* and places the encoded file in the *encoded* subdirectory.

```python
python3 main.py encoded decoded --decode
```
decodes the *encoded* subdirectory and places the output in the *decoded* subfolder.


## General

```
usage: main.py [-h] [--encode] [--decode] source destination

Encode files into {tab,space} binary.

positional arguments:
  source       Path of file or folder that serves as source for conversion.
  destination  Path of folder that serves as target for conversion.

options:
  -h, --help   show this help message and exit
  --encode     Encode source to destination.
  --decode     Encode source to destination.
  ```