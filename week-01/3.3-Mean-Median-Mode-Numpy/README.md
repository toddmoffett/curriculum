---
title: Math Primer 1 + Intro to `numpy`
type: lesson
duration: "1:5"
creator:
    name: Joshua Cook
    city: Santa Monica
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Math Primer 1
Week 1 | Lesson 3.3

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Understand the measures of Central Tendency (mean, median, and mode)
- Understand how mean, median and mode are affected by skewness in data
- Understand measures of variability (variance and standard deviation)

------

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   |  Descriptive Statistics |
| 20 min  | [Demo / Guided Practice](#demo)  | Mean, Median, and Mode  |
| 20 min  | [Demo / Guided Practice](#demo)  | Skewness  |
| 20 min  | [Demo / Guided Practice](#demo)  | Range, Variance and Standard Deviation  |
| 20 min  | [Independent Practice](#ind-practice)  |   |
| 5 min  | [Conclusion](#conclusion)  |   |

---

<a name="Descriptive Statistics"></a>
## Introduction: Stats review  (5 mins)

There are two main fields of statistics: **descriptive** and **inferential**.

--

Right now, we're going to focus on descriptive statistics: describing, summarizing, and
understanding data.

--

Our focus today is on the **Measures of Central Tendency** Measures of Central Tendency provide descriptive information about the single numerical value that is considered to be the most typical of the values of a quantitative variable.

---

<a name="Descriptive Statistics"></a>
## Introduction: Stats review  (5 mins)

There are two main fields of statistics: **descriptive** and **inferential**.

Right now, we're going to focus on descriptive statistics: describing, summarizing, and
understanding data.

That may sound complicated, but you're probably already familiar with some measures of central tendency: the **mean**, **median**, and **mode**.

--

We'll also discuss **skewness**, which is the lack of symmetry in a distribution data that affects the mean, median, and mode.

--

Lastly we'll take a look at measures of variability, namely the **range**, **variance**, and **standard deviation**.

---

<a name="Mean, median, and mode"></a>
## Guided Practice: Mean, median, and mode (20 mins)

---

### Mean

The **mean** is the sum of the numbers divided by the length of the list.

--

#### calculate the mean

```python
>>> this_list = [2,2,3,4,5]
```

--

```python
>>> this_list_mean = sum(n)/len(n)
```

--

```python
>>> print this_list_mean
3
```

##### PAIR-SHARE: SOMETHING'S WRONG!

How can we fix it?

---

### Median

For odd-length lists: the median is the middle number of the ordered list.

#### Find the median of an odd-length list

```python
>>> this_list_odd = [1,8,5,9,2,3,10,15,7]
```
--
```python
>>> this_odd_list.sort()
```
--

```python
>>> middle_index = len(n_odd)/2
```

--

```python
>>> this_odd_list_median = this_odd_list[middle_index]
>>> print this_odd_list_median
7
```

---

### Median

For even-length lists: the median is the average of the two middle numbers of the ordered list.


```python
>>> this_even_list = [8,2,3,1,0,-1,-5,20]
```

--

```python
>>> this_even_list.sort()
```

--

```python
>>> middle_index_r = len(this_even_list)/2
>>> middle_index_l = middle_index_r - 1
```

--

```python
>>> sum_of_medians = this_even_list[middle_index_r] + \
                        this_even_list[middle_index_l]
```

--

```python
>>> this_even_list_median = float(sum_of_medians)/2
```

--

```python
>>> print this_even_list_median
1.5
```

---

### DESKCHECK

_In English, write the steps required to find the median of an even-length list_.


---

### Mode

_The mode is the most frequently occurring number._

--

Finding the mode is not as trivial as the mean or median, so here it is calculated using `scipy.stats.mode()`.

Note: doing this without `scipy.stats.mode()` is a challenge problem in the independent practice section.

--

```python
>>> from scipy.stats import mode
>>> this_list = [0,1,1,2,2,2,2,3,3,4,4,4,5]
```

--

```python
>>> this_list_mode = mode(n)
```

--

```python
>>> print(this_list_mode)
(array([ 2.]), array([ 4.]))
```

--

##### WHAT IS BEING DISPLAYED HERE?

--

Write a print statement to show the **mode** on your desk.

---

### Numerical Python aka `numpy`

`numpy` and `scipy` come with convenience functions to calculate these values for you.

```python
from numpy import mean, median
from scipy.stats import mode

this_list = [3, 75, 98, 2, 10, 3, 14, 99, 44, 25,
     31, 100, 356, 4, 23, 55, 327, 64, 6, 20]

print(mean(n))
67.950000000000003

print(median(n))
28.0

print(mode(n))
ModeResult(mode=array([3]), count=array([2]))
```

---

<a name="Skewness"></a>
## Guided Practice: Skewness (20 mins)

**Skewness** is lack of symmetry in a distribution of data.

[Technical note: we will be talking about skewness here in the context of _unimodal_ distributions.]

---

.height_300_image[![](./assets/images/skewness.png)]

--

A **positive-skewed** distribution means the right side tail of the distribution is longer or fatter than the left.

--

Likewise a **negative-skewed** distribution means the left side tail is longer or fatter than the right.

--

Symmetric distributions have no skewness!

---

### Skewness and measures of central tendency

The mean, median, and mode are affected by skewness.

--

When a distribution is symmetrical, the mean, median, and mode are the same number.

--

When a distribution is negatively skewed, the mean is less than the median, which is less than the mode.

--

**Negative skew: mean < median < mode**

--

When a distribution is positively skewed, the mean is greater than the median, which is greater than the mode!

--

**Positive skew: mode < median < mean**

---

This way of thinking can help you, especially if you can't see a line graph of the data. All you need are the mean and the median. Nice!

1. If the mean < median, the data are skewed left.
2. If the mean > median, the data are skewed right.

--

##### WHAT IS THE SKEWNESS OF THIS LIST?

```python
this_list = [3, 75, 98, 2, 10, 3,14, -99, 44, 25, 31,
     100, 35, 4, 3, 55, -56, 64, 6, -330]
```

---

<a name="Range, Variance and Standard Deviation"></a>
## Guided Practice: Range, Variance and Standard Deviation (20 mins)

--

Measures of variability like the **range**, **variance**, and **standard deviation** tell you about the spread of your data.

--

These measurements give complementary (and no less important!) information to the measures of central tendency (mean, median, mode).

---

### Range

The **range** is the difference between the lowest and highest values of a distribution.

--

```python
this_list = [3, 75, 98, 2, 10, 3, 14, 99, 44,
     25, 31, 100, 356, 4, 23, 55, 327, 64, 6, 20]
```

--

```python
lower_bound = min(n)
upper_bound = max(n)
```

--

```python
this_list_range = upper_bound - lower_bound
print(this_list_range)
354
```

--

Alternatively,

```python
this_list_range = np.ptp(n)
print(this_list_range)
354
```

---

### List Comprehension

Python has a unique functional-style structure called **list comprehensions**.

--

We will spend more time with them later this week. For now, we have a brief
introduction.


This is the standard form of a list comprehension.

```python
>>> this_list = [1,2,3,4,5]
>>> this_list_squared = [x**2 for x in this_list]
```

---

### Variance

The **variance** is a numeric value used to describe how widely the numbers distribution vary.

Here we will represent the variance as:

$$\sigma^2 = \frac{1}{n}\sum (x_i - \mu)^2$$

where $\mu$ is the mean of a set of numbers.

**Note:** $\sigma^2$ is the variance. $\sigma$ is the **standard deviation**.

---

### Variance

Let's use a list comprehension to calculate the variance.
```python
this_list = [3, 75, 98, 2, 10, 3, 14, 99, 44,
     25, 31, 100, 356, 4, 23, 55, 327, 64, 6, 20]
```

--

```python
mu = np.mean(this_list)
```

--

```python
squared_differences = [(x - mu)**2 for x in this_list]
```

--

```python
sum_of_squared_differences = sum(squared_differences)
```

--

```python
n = len(this_list)
```

--

```python
sigma = sum_of_squared_differences/n
```

Which is **the average of the sum of the squared distances of each number from the mean of the numbers.**

---

**Check:** What could a distribution with a large variance look like? A small?

--

**Check:** What does a variance of 0 mean?

--

Using numpy the variance is simply:
```python
>>> variance = np.var(n)
>>> print(variance)
9414.6475
```

---

### Standard deviation

The **standard deviation** is the square root of the variance.

Because the variance is the average of the distances from the mean _squared_,
the standard deviation tells us approximately, on average, the distance of
numbers in a distribution from the mean.

The standard deviation can be calculated with:
```python
>>> std = np.std(n)
>>> print(std)
97.029106457804716
```

---

![](./assets/images/dist_with_var_std.png)

**Check:** Is this the same as the average of the absolute deviations from the mean? If not, what is the difference between the measures?

---

<a name="ind-practice"></a>
## Independent Practice: Topic (20 minutes)

- With the provided data, determine the mean, median, and mode.
- Is the data skewed left or right? How do you know?
- Find the range, variance and standard deviation of your data set. What does the standard deviation tell you about the distribution?
- Challenge: calculate the mode without using scipy!

```python
this_list = [
 6, 41,  4, 73, 25,  6, 10, 11, 91, 20, 33, 93, 95, 92, 29, 30, 26, 62,
82, 70, 68, 56, 15, 19, 51, 23, 43, 68, 82, 96, 86, 92, 46, 78, 45, 92,
52, 37, 89, 64, 68, 95, 63, 87, 26, 82, 14, 76, 62, 52, 84, 10, 50, 14,
52, 67,  9, 91, 16, 62, 47, 55, 36,  7, 61, 72, 95, 35, 86, 17, 81, 86,
94, 66, 97, 52, 31, 29, 43, 62, 78, 70, 48, 22, 79, 75, 86, 39, 42, 48,
84, 71,  5, 82, 57, 68, 99, 71, 44, 94
]
```

---

<a name="conclusion"></a>
## Conclusion (5 mins)

- Review & recap
- Q & A
