"""Service module 22561: business logic, no crypto."""


def calculate_total_22561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22561():
    return 'module 22561 handles orders and invoices'
