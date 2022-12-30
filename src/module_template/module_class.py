"""This is just a sample module to show the implementation."""
class SampleClass:
    """This is a sample class within the sample module that gets instatiated in the app.py.
    """
    def sample_method(self):
        """A sample method that can be executed by objects of this class.

        Returns:
            string: A sample string that can be returned
        """
        return "sample method executed"

    def sample_add(self, number_one: int, number_two: int):
        """A sample method that adds 2 integers to show how the testing works.

        Args:
            number_one (int): first number to be added.
            number_two (int): second number to be added.

        Returns:
            int: sum of a and b.
        """
        return number_one+number_two
