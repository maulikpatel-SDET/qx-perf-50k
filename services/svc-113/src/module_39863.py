"""Service module 39863: business logic, no crypto."""


def calculate_total_39863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39863():
    return 'module 39863 handles orders and invoices'
