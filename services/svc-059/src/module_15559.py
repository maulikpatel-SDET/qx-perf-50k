"""Service module 15559: business logic, no crypto."""


def calculate_total_15559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15559():
    return 'module 15559 handles orders and invoices'
