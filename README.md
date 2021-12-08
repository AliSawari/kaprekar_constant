# Kaprekar's Constant 6174

There is a rule in Math that applies to 4 digit numbers. for each 4 digit number
that is not made of all repetitive numbers (like 1111 or 2222), if you subtract the ascending order of that number from the descending order of it, it will eventually end up in Kaprekar's Constant which is 6174.

let's take 3870. if we take the ascending order from the descending one, and repeat the whole process we will get this:

8730 - 0378 = 8352

repeat the process

8532 - 2358 = 6174


# Run the Code
This simple code takes any number as an input and calculate how many times it takes to reaches the constant

```sh
$ python ./kaprekar_constant.py 1234
```



This Video was inspired by [Numberphile's Video](https://youtu.be/d8TRcZklX_Q)