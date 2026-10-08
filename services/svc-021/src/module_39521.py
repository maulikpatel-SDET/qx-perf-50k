"""Service module 39521: business logic, no crypto."""


def calculate_total_39521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39521():
    return 'module 39521 handles orders and invoices'
