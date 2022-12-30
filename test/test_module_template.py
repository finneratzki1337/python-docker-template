"""Sample tests for the module template."""
from src.module_template.module_class import SampleClass

def test_sample_function():
    """Testing if sample method returns a string.
    """
    my_object = SampleClass()
    assert isinstance(my_object.sample_method(), str)

def test_adding_numbers():
    """Testing if 2 inputs return an expected output."""
    my_object = SampleClass()
    assert my_object.sample_add(1, 2) == 3
