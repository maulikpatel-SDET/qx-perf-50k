"""Service module 39013: business logic, no crypto."""


def calculate_total_39013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39013():
    return 'module 39013 handles orders and invoices'
