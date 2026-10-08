"""Service module 39416: business logic, no crypto."""


def calculate_total_39416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39416():
    return 'module 39416 handles orders and invoices'
