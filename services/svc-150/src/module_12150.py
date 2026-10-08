"""Service module 12150: business logic, no crypto."""


def calculate_total_12150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12150():
    return 'module 12150 handles orders and invoices'
