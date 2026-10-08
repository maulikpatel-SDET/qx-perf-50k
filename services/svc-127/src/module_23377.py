"""Service module 23377: business logic, no crypto."""


def calculate_total_23377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23377():
    return 'module 23377 handles orders and invoices'
