"""Service module 25863: business logic, no crypto."""


def calculate_total_25863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25863():
    return 'module 25863 handles orders and invoices'
