"""Service module 35081: business logic, no crypto."""


def calculate_total_35081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35081():
    return 'module 35081 handles orders and invoices'
