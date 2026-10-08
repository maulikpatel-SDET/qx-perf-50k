"""Service module 26650: business logic, no crypto."""


def calculate_total_26650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26650():
    return 'module 26650 handles orders and invoices'
