##### Opening Hours

A program that takes JSON-formatted opening hours of a restaurant as an input 
and outputs hours in more human readable format.

I assumed we should not output a day at all, if a corresponding key is not present in the input data.

###### To run project:

- Run server.py (This will start server on port 8000. Change port in source code if needed)
- Please use Python 3. Legacy Python is not supported.
- Please use unix-based OS (MacOS or Linux). Not tested on Windows.
- To test run tests.py

I wanted to keep the code concise, simple, and free of external dependencies.
In the real life I could use py.test as the testing framework and Flask as HTTP server.

##### Thoughts about the JSON input format

It is fine, although ambiguity and can be reduced using implicit information. <br />
For example, we can make a flat array:

```
[
    <timestamp>: <event type>,
    <timestamp>: <event type>,
    ...
]
```

**\<timestamp\>**: number of seconds passed from the beginning of the week <br />
**\<event type\>**: either open or close

That way we will still know what day of the week it is (from timestamp).

We can also use binary format with schema, like protobuf/Cap'n Proto/FlatBuffers.