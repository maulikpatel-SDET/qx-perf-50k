"""Service module 18051: business logic, no crypto."""


def calculate_total_18051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18051():
    return 'module 18051 handles orders and invoices'
