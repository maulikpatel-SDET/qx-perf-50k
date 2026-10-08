"""Service module 33674: business logic, no crypto."""


def calculate_total_33674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33674():
    return 'module 33674 handles orders and invoices'
