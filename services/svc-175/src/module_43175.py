"""Service module 43175: business logic, no crypto."""


def calculate_total_43175(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43175():
    return 'module 43175 handles orders and invoices'
