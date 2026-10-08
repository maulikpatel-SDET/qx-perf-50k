"""Service module 11150: business logic, no crypto."""


def calculate_total_11150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11150():
    return 'module 11150 handles orders and invoices'
