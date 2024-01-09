A stack is a collection of objects that are inserted and removed according to the last-in, first-out (LIFO) principle.

**Example**: Internet Web browsers store the addresses of recently visited sites in a stack. 
Each time a user visits a new site, that site’s address is “pushed” onto the stack of addresses. 
The browser then allows the user to “pop” back to previously visited sites using the “back” button.

A stack is an abstract data type (ADT) such that an instance S supports the following two methods:
- S.push(e): Add element e to the top of stack S.
- S.pop(): Remove and return the top element from the stack S; an error occurs if the stack is empty.

Here defined the following accessor methods for convenience:
- S.top(): Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
- S.is empty( ): Return True if stack S does not contain any elements.
- len(S): Return the number of elements in stack S; in Python, we implement this with the special method \__len__.