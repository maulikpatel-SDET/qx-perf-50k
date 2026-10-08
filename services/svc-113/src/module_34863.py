"""Service module 34863: business logic, no crypto."""


def calculate_total_34863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34863():
    return 'module 34863 handles orders and invoices'
