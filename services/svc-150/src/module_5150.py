"""Service module 5150: business logic, no crypto."""


def calculate_total_5150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5150():
    return 'module 5150 handles orders and invoices'
