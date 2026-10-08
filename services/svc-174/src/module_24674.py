"""Service module 24674: business logic, no crypto."""


def calculate_total_24674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24674():
    return 'module 24674 handles orders and invoices'
