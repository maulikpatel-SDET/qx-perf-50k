"""Service module 18674: business logic, no crypto."""


def calculate_total_18674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18674():
    return 'module 18674 handles orders and invoices'
