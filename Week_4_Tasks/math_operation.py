def basic_operations(a, b):
    try:
       
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b

       
        return {
            'addition': addition,
            'subtraction': subtraction,
            'multiplication': multiplication,
            'division': division
        }
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: {str(e)}"


def power_operation(base, exponent, **kwargs):
    try:
        
        result = base ** exponent

       
        modulo_value = kwargs.get('modulo')
        if modulo_value is not None:
            result %= modulo_value

        return result
    except Exception as e:
        return f"Error: {str(e)}"


def apply_operations(operation_list):
    try:
       
        results = list(map(lambda x: x[0](*x[1]), operation_list))
        return results
    except Exception as e:
        return f"Error: {str(e)}"

