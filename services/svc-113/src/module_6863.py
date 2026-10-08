"""Service module 6863: business logic, no crypto."""


def calculate_total_6863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6863():
    return 'module 6863 handles orders and invoices'
