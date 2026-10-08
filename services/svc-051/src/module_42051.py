"""Service module 42051: business logic, no crypto."""


def calculate_total_42051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42051():
    return 'module 42051 handles orders and invoices'
