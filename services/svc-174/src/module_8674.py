"""Service module 8674: business logic, no crypto."""


def calculate_total_8674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8674():
    return 'module 8674 handles orders and invoices'
