from support.assertion_errors import AssertionErrors

class Assertion:
    @staticmethod
    def assertion_equal(expected, actual):
        """
        Comparison of actual and expected result
        :param actual: the result that is now
        :param expected: the result we want to get
        :return: compliance or non-compliance of the actual result with the expected
        """
        assert actual == expected, AssertionErrors.ASSERT_EQUAL.format(expected, actual)