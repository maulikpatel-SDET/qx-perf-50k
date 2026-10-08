"""Service module 30292: business logic, no crypto."""


def calculate_total_30292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30292():
    return 'module 30292 handles orders and invoices'
