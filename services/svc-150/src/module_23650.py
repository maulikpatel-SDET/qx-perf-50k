"""Service module 23650: business logic, no crypto."""


def calculate_total_23650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23650():
    return 'module 23650 handles orders and invoices'
