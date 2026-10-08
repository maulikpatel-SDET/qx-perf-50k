"""Service module 13382: business logic, no crypto."""


def calculate_total_13382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13382():
    return 'module 13382 handles orders and invoices'
