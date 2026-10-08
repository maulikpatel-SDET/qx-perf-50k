"""Service module 35382: business logic, no crypto."""


def calculate_total_35382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35382():
    return 'module 35382 handles orders and invoices'
