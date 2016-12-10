---
title: Intro to Python 2: Lists & Dictionaries
type: lesson
duration: "1:30"
creator:
    name: Lucy Williams & Kiefer Katovich
    city: DC & SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Lists & Dictionaries
Week 1 | Lesson 1.4

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Create lists and operate on them
- Create dictionaries and operate on them

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Define/describe/explain a list and a dictionary

------

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 10 min  | [Introduction](#introduction)   | Lists and dictionaries  |
| 25 min  | [Demo / Guided Practice](#demo)  | Lists  |
| 10 min  | [Independent Practice](#ind-practice)  | Lists  |
| 25 min  | [Demo / Guided Practice](#demo)  | Dictionaries  |
| 10 min  | [Independent Practice](#ind-practice)  | Dictionaries  |
| 10 min  | [Conclusion](#conclusion)  |  |

---

<a name="introduction"></a>
## Introduction: Lists and dictionaries (10 mins)

**Lists** are lists of arbitrary items in python.

Lists are:

- a compound data type
- expressed as a list of comma-separated values between brackets `[]`
- indexed starting at 0
- "mutable", meaning they can be modified such as appended to
- can contain any type of python type
- can contain a mixture of types

---

#### Examples

```python
numbers = [1, 2, 3, 4, 5]
letters = ['a','b','c','d']
mixture = ['hi',12.13,1,(1,2),['a','b','c']]
```

---

**Dictionaries** contain multiple items, like lists, but are organized in key:value pairs

Dictionaries are:

- a compound data type
- an unordered list of `key:value` pairs
- expressed with braces: `{ }`
- follow the pattern: `{ key1:value1, key2:value2, ...}`
- indexed by their keys rather than numeric index
- are mutable
- can contain mixtures of key and value types

---

#### Examples

```python
telephone_nums = {'john':5103315523, 'andrew':4156678890}
lists = {0:[1,2,3], 1:[4,5,6]}
mixture = {'animals':['dog','cat'], 1:2, empty_dicts:{'a':{}, 'b':{}}}
```

---

<a name="demo"></a>
## Demo / Guided Practice: Lists (25 mins)

In nearly all cases lists are preferable to tuples because we can change their values. Let's practice creating and modifying python lists

---

### Creating lists

Lists are defined like tuples.
Say you have 5 gryffindors called Harry, Ron, Hermione, Neville and Lavender. Create a list named "gryffindors" with the 5 `gryffindors`.

Lists can be assigned to variables. Make the list of `gryffindors` and assign it to a variable named "gryffindors"

>  L-1: make a list with the 5 `gryffindors`

```python
gryffindors = ['Harry', 'Ron', 'Hermione', 'Neville', 'Lavender']
print(gryffindors)
['Harry', 'Ron', 'Hermione', 'Neville', 'Lavender']
```

---

Recall that lists are indexed with integers.

>  L-2: print the 3rd item of the `gryffindors` list

```python
print(gryffindors[2])
Hermione
```

---

### Slicing A List

You can use two indices separated by a colon to access a range of elements within a list. This is called **slicing**.

For example: `my_list[0:5]` would print out the first 5 elements of my_list.

>  L-3: print the 3rd thru 5th elements of the `gryffindors` list

```python
print(gryffindors[2:5])
['Hermione', 'Neville', 'Lavender']
```

---

### Modifying lists

Lists have pre-defined functions which are very useful for manipulating them. The build in functions of list work _in place_, meaning that you do not have to assign the result to a new variable.

The `.append()` function will add an element to the end of a list. Use the function like: `[...].append(item)`

>  L-4: add `'Dean'` to the end of the `gryffindors` list using .append()

```python
gryffindors.append('Dean')
print(gryffindors)
['Harry', 'Ron', 'Hermione', 'Neville', 'Lavender', 'Dean']
```

---

You can also combine lists by simply adding them together with the `+` operator.

>  L-5: add the list `['Seamus', 'Parvati']` to the `gryffindors` list

```python
gryffindors = gryffindors + ['Seamus', 'Parvati']
print(gryffindors)
['Harry', 'Ron', 'Hermione', 'Neville', 'Lavender', 'Dean', 'Seamus', 'Parvati']
```

---

The `.remove()` function can remove an specific element of a list, and the `del` command will remove the item of a list at a specific index. For example, `del my_list[2]` removes the 3rd element of my_list.

>  L-6: remove 'Dean' from the list with the .remove() function

```python
gryffindors.remove(5)
print(gryffindors)
['Harry', 'Ron', 'Hermione', 'Lavender', 'Seamus', 'Parvati']
```


>  L-7: remove the first element of gryffindors using del

```python
del gryffindors[0]
print(gryffindors)
['Ron', 'Hermione', 'Lavender', 'Seamus', 'Parvati']
```

---

<a name="ind-practice"></a>
## Independent Practice: Lists (10 minutes)

Explore the built in functions of lists:

Use this list:  
`ravenclaws = ['Cho', 'Luna', 'Marcus', 'Anthony', 'Padma', 'Terry', 'Duncan', 'Latisha']`

- use `.append(item)` to add item to a list
- use `.extend([item1, item2])` to join another list to the end of the list
- use `.insert(index, item)` to add an item to a list at an index
- use `.remove(item)` to remove an item from a list
- use `.sort()` to sort a list
- use `.count(item)` to count the number of times an item appears in a list
- use `.index(item)` to find the index of an element in a list
- use `.pop()` to extract (and remove) the last element of a list
- use `.reverse()` to reverse a list

---

<a name="demo"></a>
## Demo / Guided Practice: Dictionaries (25 mins)

Dictionaries are useful when you want to associate items with a specific reference, or `key`. An example of this would be storing the `patroni` of Hogwart's students.

Remember that dictionaries are created with braces, using `{key:value, key2:value2}` syntax.

One potentially confusing aspect of dictionaries is that although they are created with braces `{ }`, accessing a value with a key is done using brackets `[ ]`, for example: `my_dict['key']` returns the value for `key` in `my_dict`.

---

##### Making and using dictionaries

Dictionaries are created the same as lists, with assignment to a variable. Create a dictionary called `patroni` with the following values:

- `'Harry':'Stag'`
- `'Ron':'Jack Russell Terrier'`
- `'Hermione':'Otter'`
- `'Luna':'Hare'`

>  D-1: Create the `patroni` dictionary

```python
patroni = {'Harry':'Stag',
           'Ron':'Jack Russell Terrier',
           'Ginny':'Horse',
           'Luna':'Hare'}
print(patroni)
{'Harry':'Stag', 'Ron':'Jack Russell Terrier', 'Ginny':'Horse',
'Luna':'Hare'}
```

---


As you can see, when you print the dictionary, the key:value pairs are not guaranteed to be ordered the way you entered them like a list.

Values for a key can be accessed using the square bracket `[ ]` syntax or with the `.get()` method.

>  D-2: access the patronus for Ron and assign it to a variable

```python
Ron = patroni['Ron']
print(Ron)
'Jack Russell Terrier'
```

---

You can list the current keys in a dictionary with the `.keys()` function. The keys will be returned in a list.

>  D-3: print out a list of the keys in `patroni` using `.keys()`

```python
patroni.keys()
['Ron', 'Harry', 'Luna', 'Ginny']
```


The `.items()` function will create a list of tuples, where each of the tuples in the list is a `key:value` pair in the dictionary.

>  D-4: print out a list of the key:value pairs in `patroni` using `.items()`

```python
patroni.items()
[('Ron', 'Jack Russell Terrier'), ('Harry', 'Stag'), ('Luna', 'Hare'), ('Ginny', 'Horse')]
```

---

##### Modifying dictionaries

Adding new `key:value` pairs to a dictionary is similar to how you access an existing entry. The syntax for adding a new entry is: `my_dict['new_key'] = new_value`.

>  D-5: add `'Hermione':'Otter'` to the `patroni` dictionary

```python
patroni['Luna'] = 'Hare'
print(patroni)
{'Ron': 'Jack Russell Terrier', 'Harry': 'Stag', 'Hermione':'Otter',
'Luna': 'Hare', 'Ginny': 'Horse'}
```

---

Removing a dictionary key:value pair can be done with the `del` command, like with a list, or with the `.pop()` function which will remove a key from the dictionary and return the value for that key.

>  D-6: remove the Luna zipcode with .pop() and assign it to a variable

```python
Luna = patroni.pop('Luna')
print(Luna)
'Hare'
```



---

<a name="ind-practice"></a>
## Independent Practice: Dictionaries (10 minutes)

Build your a dictionary of student information representing
species, gender, and graduation year:

- `'Ginny Weasley' : ('Human', 0, 1999)`
- `'Hermione Granger' : ('Human', 0, 1999)`
- `'Sirius Black' : ('Human', 1, 1978)`
- `'Bellatrix Lestrange' : ('Human', 0, 1969)`
- `'Ron Weasley' : ('Human', 1, None)`
- `'Rubeus Hagrid' : ('Half-Giant', 1, None)`
- `'Albus Dumbledore' : ('Human', 1, 1858)`
- `'Tom Riddle' : ('Human', 1, 1945)`

---

Explore some of the built in functions for dictionaries:

- use `.pop(key)` to remove a key:value pair from the dictionary and return the value
- use `.get(key)` to get the value for a key
- use `.has_key(key)` to check if a key is in the dictionary
- use `.keys()` to get a list of the keys in the dictionary
- use `.items()` to get a list of the key:value pairs in the dictionary
- use `.update(other_dictionary)` to merge a 2nd dictionary into the current dictionary
- use `.clear()` to remove all key:value pairs from the dictionary

---

<a name="conclusion"></a>
## Conclusion (10 mins)
- Partner up and explain what a list and a dictionary are to your partners
- What are the differences between a list and a dictionary?
- What are the two things you need for a dictionary?

## Bonus Challenges
Once you've mastered the basics, further your understanding of Python by attempting "[Alternate Code Challenges 2](code/starter-code/w1-1.4-bonus-starter.ipynb)".
