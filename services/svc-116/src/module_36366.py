"""Service module 36366: business logic, no crypto."""


def calculate_total_36366(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36366():
    return 'module 36366 handles orders and invoices'
