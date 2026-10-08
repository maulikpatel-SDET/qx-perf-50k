"""Service module 10561: business logic, no crypto."""


def calculate_total_10561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10561():
    return 'module 10561 handles orders and invoices'
