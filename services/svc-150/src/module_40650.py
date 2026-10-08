"""Service module 40650: business logic, no crypto."""


def calculate_total_40650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40650():
    return 'module 40650 handles orders and invoices'
