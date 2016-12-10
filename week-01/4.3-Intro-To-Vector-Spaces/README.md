---
title: Introduction to Vector Spaces
duration: "1:5"
creator:
    name: Joshua Cook
    city: Santa Monica
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to Vector Spaces
Week 1 | Lesson 4.3

### Learning Objectives

1. Represent a SQL table using a matrix and explain the significance of a **Row Vector** and a **Column Vector**
2. Perform an aaxpy using two vectors
3. Explain why the result of an axpy is in the **Vector Space**

---

### Word Wall

| | | | | |
|-|-|-|-|-|
| matrix | array | tensor | vector | inner product |
| "closed under" | scalar multiplication | vector addition | dimension | rank 
| scalar | norm | vector space |  $\mathbb{R}^n$ | linear combination | 

---

## Scientific Fact

---

## Scientific Fact

People hate linear algebra because they didn't have `numpy`.

---

## Create a SQL Table

Consider the Fisher Iris data, here retrieved from UCI's Machine Learning Data [repository](http://archive.ics.uci.edu/ml/datasets/Iris).

![](http://tinyurl.com/jcdbimg/fisher_data.png)


```
CREATE TABLE irises (
    sepal_length DOUBLE PRECISION, 
    sepal_width DOUBLE PRECISION,
    petal_length DOUBLE PRECISION,
    petal_width DOUBLE PRECISION,
    classification TEXT
);
```

---

### `irises`

`SELECT * FROM irises LIMIT 4;`

|`s_l` |`s_w` |`p_l` |`p_w` |`cl`|
|:-:|:-:|:-:|:-:|:-:|
|5.1|3.5|1.4|0.2|Iris-setosa|
|4.9|3.0|1.4|0.2|Iris-setosa|
|4.7|3.2|1.3|0.2|Iris-setosa|
|4.6|3.1|1.5|0.2|Iris-setosa|

---

## arrays and matrices

Let's leave array undefined, and use our intuitive understanding of what an array is. Later, we will explicitly define an `array` in the context of `numpy`.


### def: matrix

a rectangular array of numbers, symbols, or expressions arranged in rows or columns

---

## the standard matrix <br> representation of a SQL table

- each *row* is an instance
- each *column* is a feature

---

### `irises`

`SELECT * FROM irises LIMIT 4;`

|`s_l` |`s_w` |`p_l` |`p_w` |`cl`|
|:-:|:-:|:-:|:-:|:-:|
|5.1|3.5|1.4|0.2|Iris-setosa|
|4.9|3.0|1.4|0.2|Iris-setosa|
|4.7|3.2|1.3|0.2|Iris-setosa|
|4.6|3.1|1.5|0.2|Iris-setosa|

<br>

#### IDENTIFY AN INSTANCE

---

### `irises`

`SELECT * FROM irises LIMIT 4;`

|`s_l` |`s_w` |`p_l` |`p_w` |`cl`|
|:-:|:-:|:-:|:-:|:-:|
|5.1|3.5|1.4|0.2|Iris-setosa|
|4.9|3.0|1.4|0.2|Iris-setosa|
|4.7|3.2|1.3|0.2|Iris-setosa|
|4.6|3.1|1.5|0.2|Iris-setosa|

<br>

#### IDENTIFY A FEATURE

---

### Check For Understanding

`DROP classification FROM irises;`

|`s_l` |`s_w` |`p_l` |`p_w` |
|:-:|:-:|:-:|:-:|
|5.1|3.5|1.4|0.2|
|4.9|3.0|1.4|0.2|
|4.7|3.2|1.3|0.2|
|4.6|3.1|1.5|0.2|

<br>

#### Represent this `select` as a matrix

On your desk represent this `select` statement using a matrix.

---

## Dimension and Rank

| | | |
|-|-|-|
| $\left(\begin{matrix}\left(\begin{matrix}1 && -1 \\ -1 && 1 \end{matrix}\right) && \left(\begin{matrix}-1 && 1 \\ 1 && -1\end{matrix}\right) \\ \left(\begin{matrix}-1 && 1 \\ 1 && -1\end{matrix}\right) && \left(\begin{matrix}1 && -1 \\ -1 && 1 \end{matrix}\right)\end{matrix}\right)$ | $\left(\begin{matrix}4\end{matrix}\right)$ | $\left(\begin{matrix}1 , 1 , -1\end{matrix}\right)$ 
 $\left(\begin{matrix}1 & 0 & 1 \\0 & 0 & 1 \\ 1 & 1 &  -1\end{matrix}\right)$ |$\left(\begin{matrix}1 \\ 1 \\ -1\end{matrix}\right)$ | $e$ |

---

## Dimension and Rank

**dimension** corresponds to `numpy.shape` and describes the shape of the array

**rank** corresponds to the dimension of `numpy.shape` and describes the `type` of the array

---

## Take a row vector from `irises`

|`s_l` |`s_w` |`p_l` |`p_w` |
|:-:|:-:|:-:|:-:|
|5.1|3.5|1.4|0.2|
|4.9|3.0|1.4|0.2|
|4.7|3.2|1.3|0.2|
|4.6|3.1|1.5|0.2|

$$row_1 = (5.1, 3.5, 1.4, 0.2) $$

##### WHAT IS ITS DIMENSION? RANK?

---

## Take a column vector from `irises`

|`s_l` |`s_w` |`p_l` |`p_w` |
|:-:|:-:|:-:|:-:|
|5.1|3.5|1.4|0.2|
|4.9|3.0|1.4|0.2|
|4.7|3.2|1.3|0.2|
|4.6|3.1|1.5|0.2|

$$col_1 = (5.1, 4.9, 4.7, 4.6)$$

##### WHAT IS ITS DIMENSION? RANK?

---

## A note on vectors

You will often see a vector represented like this:

$$(5.1, 4.9, 4.7, 4.6)^T=\left(\begin{matrix}5.1\\ 4.9\\ 4.7\\ 4.6\end{matrix}\right)$$

---

##### THIS IS PEDANTRY

![](http://tinyurl.com/jcdbimg/wc_pedantry.jpg)

---

## Representing Arrays

You can use brackets or parentheses around your vectors.

You can represent your vectors (1-tensors) however you like. `numpy` will usually intuit the correct multiplication. 

---

## Vector Spaces

Consider these sets of vectors:

|||
|-|-|
|$(1),(3),(e)$| elements of $\mathbb{R}$|
|$(0,1),(-2,3),(e,\pi)$| elements of $\mathbb{R}^2$|
|$(1,0,1),(1,2,3),(e,e,e)$| elements of $\mathbb{R}^3$|

---

## Visualization of $\mathbb{R}$

![](http://tinyurl.com/jcdbimg/r1.png)

---

## Visualization of $\mathbb{R}^2$

![](http://tinyurl.com/jcdbimg/r2.png)

---

## Visualization of $\mathbb{R}^3$


![](http://tinyurl.com/jcdbimg/r3.png)

---

## Vector Spaces

$\mathbb{R}$,  $\mathbb{R}^2$, $\mathbb{R}^3$ are *vector spaces*. 

---

## Vector Spaces

$\mathbb{R}$,  $\mathbb{R}^2$, $\mathbb{R}^3$ are *vector spaces*. 

Actually, the only vector spaces that are easily visualized.

We are working toward the definition of a vector space.

---

## def: scalar multiplication

We will not formally define scalar multiplication and just go with an intuitive understanding. 

$$3\left(\begin{matrix}2 \\ 1\end{matrix}\right)
=\left(\begin{matrix}6 \\ 3\end{matrix}\right)$$

Scalar multiplication requires that the scalar be multiplied to every element in the object. 

---

## def: scalar multiplication

We will not formally define scalar multiplication and just go with an intuitive understanding. 

$$3\left(\begin{matrix}2 & 3 \\ 1 & -1\end{matrix}\right)
=\left(\begin{matrix}6 & 9\\ 3 & -3 \end{matrix}\right)$$

Scalar multiplication requires that the scalar be multiplied to every element in the object. 

---

## def: vector addition

We will not formally define vector addition and just go with an intuitive understanding. 

$$
\left(\begin{matrix}2 \\ 1\end{matrix}\right)+\left(\begin{matrix}3 \\ 3\end{matrix}\right)
=\left(\begin{matrix}5 \\ 4\end{matrix}\right)$$

Addition is *only* defined for objects of the same dimension **and** rank.

---

## def: vector space

A vector space is a set of element closed under scalar multiplication and vector addition. 


---

## def: vector space

A vector space is a set of element closed under scalar multiplication and vector addition. 

If we take an element of a vector space and perform one of these two operations on it, the result is also an element of the **same** vector space.

---

## def: vector space

All elements of a given vector space have the same **dimension** and **rank**.

---

## def: linear combination

A vector resulting from the scalar multiplication and vector addition of two vectors. 

The result is an element of the same vector space. 

---


## def: axpy

Linear combination is so common in vector arithmetic that it has a simple name: axpy

$$a\mathbf x+ \mathbf y$$

---

## Practice

Perform these linear combinations where possible:

| | |
|-|-|
| $4\left(\begin{matrix}2 \\ 1\end{matrix}\right)+\left(\begin{matrix}3 \\ 3\end{matrix}\right)$|  $e\left(\begin{matrix}1\\0\\1\end{matrix}\right)+\left(\begin{matrix}4\\2\\1\end{matrix}\right)$
| $\left(\begin{matrix}-1\\1\end{matrix}\right)\left(\begin{matrix}2\\1\end{matrix}\right)+\left(\begin{matrix}1 \\ -1\end{matrix}\right)$|  $\pi\left(\begin{matrix}2\\1\end{matrix}\right)+\left(\begin{matrix}1\\2\\-1\end{matrix}\right)$

---

## Check

*Think-Pair-Share*: Why is the result of an axpy in the same vector space?
---
