# Count frequencies

## Sample code
This repository contains some template code in a file called `frequencies.py` for a function called `frequencies`, which takes a single argument called `items`:

```
def frequencies(items):
    frequencies = {}
    # Your code goes here
    return frequencies
```

The repository also includes a file with tests called `frequencies_test.py`.  You must **not** touch this file.

## Assignment
Your assignment in this exercise is to extend the code, such that it produces a dictionary based on the `items` list.  For each item in `items`, the dictionary must contain a key.  If the item is not a string, the key must be the item converted to a string.  The value must be a positive integer counting the number of times the item represented by the key occurs in `items`.

For example,
`frequencies(['a', 'a', 'b', 'b', 'b', 'c'])`
must return the following dictionary:
`{ 'a': 2, 'b': 3, 'c': 1 }`

For example,
`frequencies([100, 'Hello', '100', '100', 100])`
must return the following dictionary:
`{ '100': 4, 'Hello': 1 }`

## How to complete the exercise
To start work on the exercise, find the URL of this repository on GitHub and clone it to your machine with:

`$ git clone URL`

where `URL` is the URL of your repository on GitHub.  Find the `frequencies.py` file and complete your solution.

You can test your solution in the development environment by running pytest.  From the root of your Python project, simply run

`$ pytest`

If pytest has not been installed yet, run:

`$ pip3 install pytest`

I recommend that you test your solution locally, but you do not have to do this.  Once your exercise is complete, you need to push your repository with:

`$ git push`

GitHub will automatically test your solution.
