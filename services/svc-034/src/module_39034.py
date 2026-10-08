"""Service module 39034: business logic, no crypto."""


def calculate_total_39034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39034():
    return 'module 39034 handles orders and invoices'
