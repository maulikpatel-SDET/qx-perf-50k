"""Service module 43809: business logic, no crypto."""


def calculate_total_43809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43809():
    return 'module 43809 handles orders and invoices'
