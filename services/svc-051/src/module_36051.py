"""Service module 36051: business logic, no crypto."""


def calculate_total_36051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36051():
    return 'module 36051 handles orders and invoices'
