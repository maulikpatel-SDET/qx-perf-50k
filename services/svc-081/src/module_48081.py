"""Service module 48081: business logic, no crypto."""


def calculate_total_48081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48081():
    return 'module 48081 handles orders and invoices'
