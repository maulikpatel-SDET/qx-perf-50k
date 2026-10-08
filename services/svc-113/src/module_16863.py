"""Service module 16863: business logic, no crypto."""


def calculate_total_16863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16863():
    return 'module 16863 handles orders and invoices'
