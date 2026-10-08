"""Service module 32051: business logic, no crypto."""


def calculate_total_32051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32051():
    return 'module 32051 handles orders and invoices'
