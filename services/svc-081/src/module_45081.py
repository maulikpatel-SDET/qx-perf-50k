"""Service module 45081: business logic, no crypto."""


def calculate_total_45081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45081():
    return 'module 45081 handles orders and invoices'
