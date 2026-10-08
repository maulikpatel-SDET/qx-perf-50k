"""Service module 23051: business logic, no crypto."""


def calculate_total_23051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23051():
    return 'module 23051 handles orders and invoices'
