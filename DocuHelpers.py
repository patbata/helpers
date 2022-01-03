# --------------------------------------------------------------------------------------
# AUTHOR: Michelle Nemiada
# DESCRIPTION: Modules for python docmentation.
# DATE CREATED: January 28, 2021
# DATE MODIFIED: January 29, 2021
# --------------------------------------------------------------------------------------

from datetime import date


class DocuHelpers:
    """Helper functions for faster documentation."""
    
    def __init__(self):
        self.today = date.today().strftime("%B %d, %Y")

    def insert_fn_to_class(self, fn_src_str='', script_filename=''):
        # Date Added/Modified: January 28, 2021
        
        """Add a function to an existing Python class.

        Parameters:
        -----------
            fn_src_str (string): source_code of the function to be added, (convert function to string using inspect.getsource(function_name))
            script_filename (str): filename of the python script that contains the class.
            
        """

        # insert indentation
        fn_src_str = '\n'.join(['    '+line for line in fn_src_str.split('\n')])

        idx = fn_src_str.index('(')+1

        # check if function is already defined in the class
        with open(script_filename, 'r') as file:
            s = file.read()
            file.close()

        try:
            if(s.index(fn_src_str[:idx])):
                raise Exception('Function already defined in class.')

        except ValueError as e:
            pass


        # add 'self' in function (since the function will be added to a class)
        fn_src_str = fn_src_str[:idx] + 'self, ' + fn_src_str[idx:]

        # add timestamp
        idx = fn_src_str.index(':')+1
        timestamp_str = '\n{0}\n{0}# Date Added/Modified: {1}    \n'.format(' '*8, self.today)
        fn_src_str = fn_src_str[:idx] + timestamp_str + fn_src_str[idx:]

        with open(script_filename, 'a+') as file:
            file.write('\n' + fn_src_str)
            file.close()

        print('Module added to class.')
        