# Basic info

Print colorful(256) tables for terminal with built-in themes: 

* dark
* blue
* red
* green

Based on tabulate 0.7.7

## requirement

Need install tabulate via pip or easy-install

```bash
    $ pip install tabulate==0.7.7
```

## usage

```python
    from ctable import table

    row = [["Alice","F",24],["Bob","M",19],["Carlos","M",19]]
    header = ['name', 'male', 'age']

    for colorfmt in ['dark', 'green', 'red', 'blue']:
        print table(row, header, colorfmt=colorfmt)
        print

```

Output 
![Result](/images/table.png)