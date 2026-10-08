"""Service module 30051: business logic, no crypto."""


def calculate_total_30051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30051():
    return 'module 30051 handles orders and invoices'
