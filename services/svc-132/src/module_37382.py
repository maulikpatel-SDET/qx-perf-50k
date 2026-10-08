"""Service module 37382: business logic, no crypto."""


def calculate_total_37382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37382():
    return 'module 37382 handles orders and invoices'
