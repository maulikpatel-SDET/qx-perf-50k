"""Service module 18366: business logic, no crypto."""


def calculate_total_18366(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18366():
    return 'module 18366 handles orders and invoices'
