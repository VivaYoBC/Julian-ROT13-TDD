After extensive and intensive research into TDD using Python, the unanimous consensus
is that the tool to use for automated suite testing is PYTEST.

1. It provides self-discovery of which functions to test based on the syntax of
	filenames.
	
2. It has its own assertion mechanism to verify correctness of results.

3. It provides parametrization to use an arbitrary number of different inputs to a procedure.

4. It creates temporary system environments to provide automatic set-up and teardown of
	environments to execute integration tests.
	
5. It provides fixture for functional tests.

-----------------------------------------------

I should mention the caveat that in my environment using Python Anaconda 3.6, many of the
research examples could not be replicated.

The most crucial concerns the impossibility to get Pytest to find and import modules or packages
containing my own sourcre code into the test files, as long as they would be theoretically 
in ANY DIRECTORY below the master node (as it should be according to the documentation).

I spent an innumerable amount of hours trying to fix this, and the best I could do was to
have the modules and the tests in the same directory.
	
	