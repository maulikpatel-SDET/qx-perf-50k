"""Service module 19051: business logic, no crypto."""


def calculate_total_19051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19051():
    return 'module 19051 handles orders and invoices'
