# **Requirements\setup.py**

  ```
     package-one==1.9.4
     git+git://github.com/path/to/package-two@41b95ec#egg=package-two
     package-three==1.0.1
  ```

# **Debug**

`dir, pdb, ipdb`

# **List\Dictionary comprehension**

* Build the following matrix using list comprehension: 
  ```
    [[ 1, 0, 0 ],
    [ 0, 1, 0 ],
    [ 0, 0, 1 ]]
  ```
* Given the list: 

  ```names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]``` 
  
  construct a new  list:
  
  * capitalize first letter
  * rest of the name in lower
  * no duplications 
  * real name (more than 1 letter) 
  
  ```['Bob', 'John', 'Alice' }``` 

* Given the dictionary:
   * create a dict with 2 keys: even and odd
   * even\odd value should be a list of all keys from the original dictionary which their value is even\odd  

  ```dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}```
 
   construct the dictionary: 
 
   ```{'even': ['b', 'd', 'f'], 'odd': ['a', 'c', 'e']}```

# **Functional programming**

* Write a decorator to print: 
   
   ```<function-name>: start\end```
   
   before and after a function is executed
* Write a factory function that according to the arguments type return a suitable sum
  ```
    [1, 2, 3, 4] --> 10
    ['k', 'e', 'r', 'e', 'n'] --> 'keren'
    ['k', 3, 'r'] --> 'k3r' (mixed become a string)
  ```