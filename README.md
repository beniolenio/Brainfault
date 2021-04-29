# Brainfault

+ = increment the cell over the pointer by 1
- = decrement the cell over the pointer by 1
. = output the current cell as an ascii character
: = output the current cell as an integer
? = output the current cell as binary
, = accept one byte of input
< = decrement the pointer
> = increment the pointer
[ = jump past the matching ']' if the cell at the pointer is 0
] = jump back to the matching '[' if the cell at the pointer is nonzero
/ = jump past the matching '|' if the length of the input queue is 0
| = jump back to the matching '/' if the length of the input queue is nonzero 
!int(instructions) = if current cell is not int, then skip to matching ')'
!~int(instructions) = if current cell is int, then skip to matching ')'
$func_name{instructions} = subroutine named func_name
*func_name* = run func_name subroutine
#comment# = comment (may or may not be multi-line)

Subroutine names can only include uppercase and lowercase letters as well as underscores

No defining subroutines in subroutines—that is to say, all subroutines are global.

Input will be in the form of an iterable which will be converted to a queue.
E.g. a list, string (if you only want to input chars), Queue, etc.
Input values can be of type char, int ( < 256 ), or binary byte ( <= 0b11111111 )

There will be infinite cells in either direction each of which can hold 8 bits, or one byte.
That is, an integer from 0 to 255, inclusive.  If a cell is incremented while its value is
255, its value wraps to 0.  If a cell is decremented while its value is 0, its value
wraps to 255.

Based on Brainfuck: https://esolangs.org/wiki/Brainfuck