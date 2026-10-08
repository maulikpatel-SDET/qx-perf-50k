"""Service module 13863: business logic, no crypto."""


def calculate_total_13863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13863():
    return 'module 13863 handles orders and invoices'
