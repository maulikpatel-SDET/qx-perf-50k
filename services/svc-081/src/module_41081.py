"""Service module 41081: business logic, no crypto."""


def calculate_total_41081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41081():
    return 'module 41081 handles orders and invoices'
