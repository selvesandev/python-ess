def my_func(a, b):
    return a + b


try:
    f = open('test.txt', 'r')
    f.write('Write a test line')
except TypeError:
    print('The was a Type Error')
except OSError:
    print('hey you have an OS Error')
else:
    # Would get executed when the try block was successful.
    print('Written successfully')
finally:
    print('I always run..')
