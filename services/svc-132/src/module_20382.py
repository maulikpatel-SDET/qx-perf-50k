"""Service module 20382: business logic, no crypto."""


def calculate_total_20382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20382():
    return 'module 20382 handles orders and invoices'
