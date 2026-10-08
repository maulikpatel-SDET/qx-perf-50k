"""Service module 20081: business logic, no crypto."""


def calculate_total_20081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20081():
    return 'module 20081 handles orders and invoices'
