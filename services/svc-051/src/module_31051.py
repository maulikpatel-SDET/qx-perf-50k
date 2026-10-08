"""Service module 31051: business logic, no crypto."""


def calculate_total_31051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31051():
    return 'module 31051 handles orders and invoices'
