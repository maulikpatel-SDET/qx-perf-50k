"""Service module 14382: business logic, no crypto."""


def calculate_total_14382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14382():
    return 'module 14382 handles orders and invoices'
