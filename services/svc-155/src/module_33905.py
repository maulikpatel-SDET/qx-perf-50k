"""Service module 33905: business logic, no crypto."""


def calculate_total_33905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33905():
    return 'module 33905 handles orders and invoices'
