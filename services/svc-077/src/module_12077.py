"""Service module 12077: business logic, no crypto."""


def calculate_total_12077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12077():
    return 'module 12077 handles orders and invoices'
