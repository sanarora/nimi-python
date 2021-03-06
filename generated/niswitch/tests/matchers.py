'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
from niswitch import visatype

# Base classes


class _ScalarMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("Unexpected type. Expected: {0}. Received: {1}".format(self.expected_type, type(other)))
            return False
        if other.value != self.expected_value:
            print("Unexpected value. Expected: {0}. Received: {1}".format(self.expected_value, other.value))
            return False
        return True


class _PointerMatcher(object):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __eq__(self, other):
        if not isinstance(other, ctypes.POINTER(self.expected_type)):
            print("Unexpected type. Expected: {0}. Received: {1}".format(ctypes.POINTER(self.expected_type), type(other)))
            return False
        return True


class _BufferMatcher(object):
    def __init__(self, expected_element_type, expected_size_or_value):
        if isinstance(expected_size_or_value, int):
            # Were given the size of the buffer
            self.expected_value = None
            self.expected_size = expected_size_or_value
        else:
            # Were given a list or something that behaves like a list
            self.expected_value = expected_size_or_value
            self.expected_size = len(expected_size_or_value)
        self.expected_type = expected_element_type * self.expected_size

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("Unexpected type. Expected: {0}. Received: {1}".format(self.expected_type, type(other)))
            return False
        if self.expected_size != len(other):
            print("Unexpected length. Expected: {0}. Received: {1}".format(self.expected_size, len(other)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for i in range(0, len(self.expected_value)):
                if self.expected_value[i] != other[i]:
                    print("Unexpected value at index {0}. Expected: {1}. Received: {2}".format(i, self.expected_value, self.expected_value))
                    return False
        return True


# Strings


class ViStringMatcher(object):
    def __init__(self, expected_string_value):
        self.expected_string_value = expected_string_value

    def __eq__(self, other):
        if not isinstance(other, ctypes.Array):
            print("Unexpected type. Expected: {0}. Received: {1}".format(ctypes.Array, type(other)))
            return False
        if len(other) < len(self.expected_string_value) + 1:  # +1 for NULL terminating character
            print("Unexpected length in C string. Expected at least: {0}. Received {1}".format(len(other), len(self.expected_string_value) + 1))
            return False
        if not isinstance(other[0], bytes):
            print("Unexpected type. Not a string. Received: {0}".format(type(other[0])))
            return False
        if other.value.decode("ascii") != self.expected_string_value:
            print("Unexpected value. Expected {0}. Received: {1}".format(self.expected_string_value, other.value.decode))
            return False
        return True


# Custom Type


class CustomTypeMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("Unexpected type. Expected: {0}. Received: {1}".format(self.expected_type, type(other)))
            return False
        # From https://stackoverflow.com/questions/20986330/print-all-fields-of-ctypes-structure-with-introspection
        for field in self.expected_value._fields_:
            field_name = field[0]
            expected_val = getattr(self.expected_value, field_name)
            other_val = getattr(other, field_name)
            if expected_val != other_val:
                print("Unexpected value field {0}. Expected: {1}. Received: {2}".format(field_name, expected_val, other_val))
                return False
        return True


# Scalars


class ViBooleanMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, visatype.ViBoolean, 1 if expected_value is True else 0)


class ViSessionMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, visatype.ViSession, expected_value)


class ViInt16Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, visatype.ViInt16, expected_value)


class ViInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, visatype.ViInt32, expected_value)


class ViInt64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, visatype.ViInt64, expected_value)


class ViReal64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, visatype.ViReal64, expected_value)


# Pointers


class ViBooleanPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, visatype.ViBoolean)


class ViSessionPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, visatype.ViSession)


class ViInt16PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, visatype.ViInt16)


class ViInt32PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, visatype.ViInt32)


class ViInt64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, visatype.ViInt64)


class ViReal64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, visatype.ViReal64)


# Buffers


class ViBooleanBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, visatype.ViBoolean, expected_size_or_value)


class ViCharBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, visatype.ViChar, expected_size_or_value)


class ViInt16BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, visatype.ViInt16, expected_size_or_value)


class ViInt32BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, visatype.ViInt32, expected_size_or_value)


class ViInt64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, visatype.ViInt64, expected_size_or_value)


class ViReal64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, visatype.ViReal64, expected_size_or_value)

