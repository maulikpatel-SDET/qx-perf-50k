"""Service module 10236: business logic, no crypto."""


def calculate_total_10236(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10236():
    return 'module 10236 handles orders and invoices'
