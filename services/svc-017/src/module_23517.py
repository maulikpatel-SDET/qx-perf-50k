"""Service module 23517: business logic, no crypto."""


def calculate_total_23517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23517():
    return 'module 23517 handles orders and invoices'
