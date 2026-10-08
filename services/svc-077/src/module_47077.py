"""Service module 47077: business logic, no crypto."""


def calculate_total_47077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47077():
    return 'module 47077 handles orders and invoices'
