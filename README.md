# Arithmetic Arranger

## Description
This Python project is part of a **FreeCodeCamp** learning challenge. It formats and displays simple arithmetic problems in a structured way, similar to how they appear on paper. The program supports addition and subtraction, ensures input validation, and optionally displays the answers.

## Features
- ✅ Supports up to **5 problems** at a time
- ✅ Validates input (**only `+` and `-`**, numbers up to **4 digits**)
- ✅ Formats problems neatly with proper spacing
- ✅ Optionally displays answers

## Example Output
### With Answers:
```python
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], show_answers=True))
```
#### Output:
```
   32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
   40     -3800     19998      474
```

### Without Answers:
```python
print(arithmetic_arranger(["32 + 8", "1 + 3801", "9999 + 2", "523 - 49"], show_answers=False))
```
#### Output:
```
   32         1      9999      523
+  8    + 3801    +    2    -  49
----    ------    ------    -----
```

