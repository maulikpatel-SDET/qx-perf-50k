"""Service module 29077: business logic, no crypto."""


def calculate_total_29077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29077():
    return 'module 29077 handles orders and invoices'
