# Generators

Generator functions allows us to write a function that can send back a value and 
then later resume to pick up where it left off.

* The basic idea is it allows us to generate a sequence of values over time.
* The main different in the syntax will be the use of `yield` statement.

* When a generator function is compiled it becomes an object that support and iteration protocol.
That means when they are called in your code they don't actually return a value and then exit.


* Generator function will automatically suspend and resume their execution and state around the last
point of value generator.

* The advantage is that instead of having to compute an entire series of values up front, the
generator computes one value waits until the next value is called for

 
