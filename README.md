# Partitions and the Collatz Conjecture

## Purpose
Sequence Analysis for the 3n+1 problem - just having fun with it

## Stuff to figure out

- Notation is still kinda janky but lets come back to it
- Unions of sequences feels odd for some reason. 
    - Implicit assumption is Unions do not retain order but sequences need this. Definition issue?

## Overview

test:
$$ f(x) = 2 $$

Define the recurrence relation
$$
f_{n+1} =  \left\{
\begin{array}{ll}
	3\cdot f_n + 1 	& \text{for } n\equiv 1 \pmod{2}\\
	f_n/2       	& \text{for } n\equiv 0 \pmod{2} 
\end{array} 
\right.
$$
The Collatz Conjecture posits that for all $i \in \mathbb{N}$ a sequence $H(i)$ with $k$ steps has $H_k$ = $1$, where each value in $H$ follows the recurrence relation $f$
$$ 
H(i) = 
\{ 
    H_0, H_{1}, ..., H_{k} | H_{k} = 1 
\}
$$

An example of this sequence $H(8)$ has $n=4$:
$$
\begin{array}{ll}
                &\{\blue{8, 4, 2, 1}, 4, 2, 1, 4, 2, 1, ...\}   \\
    H(8)     =   &\{8,4,2,1 \}                                   \\
    |H(8)|   =   & 4
\end{array}
$$

## Definitions
Commonly used words captured below
- Hailstone Sequence: also known as Path
- Step: the index of a number in a Hailstone Sequence
- Cycle: a repeated sequence of numbers contained within a sequence



## The Main Idea
Try to find sequences that have predictable number of steps until the Hailstone Sequence reaches a number less than the starting value

If all $H(k)$ are known to converge for $k < n$ and $H(n)$ has some $i$ where $H(n)_i = H(k)$ then $H(k) \subseteq H(n)$ and $H(n)$ will converge.

### Approach
Partition $\mathbb{N}$ into 3 sets $ \{2k\} \cup \{ 4k+1 \} \cup \{4k-1\} $

$$
\begin{array}{ll}
    2k      &= {2,4,6,8,10,12,14,16,18,20,...} \\
    4k+1    &= {5,9,13,17,21,25,29,...} \\
    4k-1    &= {3,7,11,15,19,23,27,...} 
\end{array}
$$
The number of steps it takes for these to reach a number in the sequence less than the start
$$
\begin{array}{ll}
    2k      &= {1,1,1,1,1,1,1,1,1,1,1,1,1,...} \\
    4k+1    &= {3,3,3,3,3,3,3,...} \\
    4k-1    &= {6,11,8,11,6,8,96,91,6,...} 
\end{array}
$$

The numbers of interest are $4k-1$ (notice 27 is on this list).


## Functions

Define the function
$$
f(n) =  \left\{
\begin{array}{ll}
	3\cdot n+1       & \text{for } n\equiv 1 \pmod{2} \\
	n/2              & \text{for } n\equiv 0 \pmod{2} 
\end{array} 
\right.
$$


## Proofs and stuff

### Idea 1
If $H(n)$ contains a convergent subset $H(k)$ then  $H(n)$ is known to converge.

**Proof** - tbc

Example:
If $H(2), H(3), ..., H(7)$ are known to converge, then $H(8)$ can be expressed as $H(8) = H(8)_0 \cup H(4)\ $ and is known to converge


### Idea 2
Where $n$ is even, $H(n)$ has $H(n)_1 < H(n)_0 $

**Proof:** 

Since $n$ is even and $H(n)_0 = n$, then $H(n)_1$ = $n/2$ which is less than $n$

Therefore $H(n)_1 < H(n)_0 $


### Idea 3
Let $\mathbb{O} = \{ 2n-1 : n \in \mathbb{N} \}$ denote the set of positive odd integers. 

For all $j \in \mathbb{N}$, it follows that $\mathbb{O}$ can be partitioned by the union of sets:
$$
    \mathbb{O} = \bigcup _{k=1}^\infty \left\{  2kj-2l+1 \right\}_{l=1}^j 
$$

**Proof:**

Probably induction but feels like a lot of work - can I be bothered?

##### Case j=1:
$$\large
    \begin{array}{ll}
    \mathbb{O} &= \bigcup _{k=1}^\infty \left\{  2k-2l+1 \right\}_{l=1}^1 \\ 
                &= \bigcup _{k=1}^\infty \left\{  2k-1 \right\} \\
                &= {1} \cup {3} \cup {5} \cup {7} \cup {...}
    \end{array}
$$

##### Assume true for j=n:
$$\large
    \mathbb{O} = \bigcup _{k=1}^\infty \left\{  2kn-2l+1 \right\}_{l=1}^1 \\ 
$$

##### Prove true for j=n+1:


## Other substitutions - probably useful

$$\large
\begin{array}{ll}
    \mathbb{O} &= \{ 2n-1 \}_{n=1}^\infty \\
                &= \lim_{n=1}^\infty \{ 2k-1 \}_{k=1}^n \\
                &= \lim_{n=1}^\infty \{1, 3, 5, ..., 2n-1\} \\
                &= \lim_{n=1}^\infty \{1, 5, 9, ..., \frac{4n}{2}-3, 3, 7, 11, ..., \frac{4n}{2}-1\} \\ 
                &= \lim_{n=1}^\infty \{ 2k-3 \}_{k=1}^n \cup \{ 2k-1 \}_{k=1}^n \\ 
                &= \{ 2k-3 \}_{k=1}^\infty \cup \{ 2k-1 \}_{k=1}^\infty  \\ 
\end{array}
$$



## ------------------------------------------------------------------------------------------------------------------------------
##

### Old notes

Assume all numbers $k$ up to some $n$ are known to converge to 1. If at some point in the path of $n$, it reaches some $k<n$, then it is part of a path that is already known to converge, so it must converge.


The numbers that do not fall into this categorisation can be found using the simple formula $4n-1$. Taking $n=7$, 27 is one of these numbers.  \\
Consider all numbers that $k$ up to $n=2a$ are known to converge (including all $4b-1<n$!!!). After a single iteration, $n_2=a<k$, so the path converges. Given that 50\% of numbers are even, if the assumption holds true for all $k<n$, all even numbers are known to converge.  \\

Now consider the remaining numbers which are odd, $2a+1$, which can be written as: 

$$4a+1$$ 
$$4a-1$$
If some odd $n$ can be found, such that it is an integer after applying the operations $\frac{3n+1}{4}$, then another portion of the naturals will converge to 1. Let $n=4a+1$ and then $n=4a-1$, and check that the results are integer: 

$$\frac{3(4a+1)+1}{4}=3a+1$$
$$\frac{3(4a-1)+1}{4}=3a-\frac{1}{2}$$

Arriving at the conclusion, that any number $n=4a+1$ will always be integer after 3 iterations (1 odd 2 even), and $n=4a-1$ will never be integer after the same 2 iterations (1 odd 2 even), for $a\in\mathbb{N}$. \\
Using the 'counter' function, this proof is seen more practically:
$$S=\{0, 1, 6, 1, 3, 1, 11, 1, 3, 1, 8, 1, 3, 1, 11, 1, 3, 1, 6, 1,...\}$$
Written again without the terms $4n-1$:
$$\{0, 1, c, 1, 3, 1, c, 1, 3, 1, c, 1, 3, 1, c, 1, 3, 1, c, 1,...\}$$
It takes 1 iteration for any $n=2a$ to be equal to some $k<n$. \\
It takes 3 iterations for any $n=4a+1$ to be equal to some $k<n$.\\
So thats 75\% done.
The function output for the other numbers seems to be more interesting:
$$S_{4a-1}=\{6, 11, 8, 11, 6, 8, 96, 91, 6, 13, 8, 88, 6, 8, 11, 88, 6, 83, 8, 13,...\}$$
Any number that appears multiple times will be left, and there might be a visible pattern in the set:
$$\{6, 11, 8, 11, 6, 8, c, c, 6, 13, 8, 88, 6, 8, c, 88, 6, c, 8, 13,...\}$$
The number 6 and the number 8 seem to appear sequentially. \\






\subsubsection{Iterations of 6}
6 appears every $4a+1$ elements in the set $S_{4a-1}$. Armed with this knowlege, the original set can be searched for the index for each appearence of 6.\\
$$S_{16a-13}=\{3, 19, 35, 51, 67,...\}$$
It should be noted that the -13 in the equation is a consequence of indexing at 1. Now consider the path of 3:
$$\{3, 10, 5, 16, 8, 4, 2, 1\}$$
Index $6 = 2 < 3$. The pattern between even and odd numbers in the equation $16a-13$ must be (1 odd, 1 even, 1 odd, 3 even). \\
Out of every 16 numbers, there will be one that is in this equation, so another $\frac{1}{16}$ of numbers have been solved. 

\subsubsection{Iterations of 8}
The spacing between indexes of 8 is alternating between gaps of 3 and 5. This suggests there are two different sequences are at play.

$$\{3, 6, 11, 14, 19, 22,...\}$$

It would make sense here to split up the even and odd indexes into two separate sets, that's likely where the different sequences come from. \\

\begin{multicols}{2}
	\noindent
	$$Odd=\{3,11,19,27,35...\}$$
	$$Even = \{6,14,22,30,38,...\}$$
\end{multicols}

These indexes correspond to $n=4(8a-5)-1$ (odd) and $n=4(8a-2)-1$ (even), so the set of $n$ from these indexes is: \\

\begin{multicols}{2}
	\noindent
	$$N_{odd}=\{11, 43, 75, 107, 139,...\}$$
	$$S_{32n-21}=\{11, 43, 75, 107, 139,...\}$$	
	$$N_{even}=\{23, 55, 87, 119, 151,...\}$$	
	$$S_{32n-9}=\{23, 55, 87, 119, 151,...\}$$
\end{multicols}Now consider the path of 11 from the odd side: 
	$$\{11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1\}$$
	Index $8 = 10 < 11$. The pattern between even and odd numbers in the equation $32a-21$ must be (1 odd, 1 even, 1 odd, 2 even, 1 odd, 2 even). \\
	Lastly considerthe path of 23 from the even side:
	$$\{23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1\}$$
	Index $8 = 20 < 23$. The pattern between even and odd numbers in the equation $32a-21$ must be (1 odd, 1 even, 1 odd, 1 even, 1 odd, 3 even). \\

Out of every 32 numbers, two of them will be from the above equations. Another $\frac{1}{16}$ of numbers have been shown to converge.
\vfill
This whole method works off the assumption that $k$ up to $n$ are already known to converge, so in order for this method to be a valid solution to The Collatz Conjecture, there must be a finite number of equations that span the naturals. 

\break
