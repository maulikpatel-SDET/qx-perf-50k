"""Service module 10081: business logic, no crypto."""


def calculate_total_10081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10081():
    return 'module 10081 handles orders and invoices'
