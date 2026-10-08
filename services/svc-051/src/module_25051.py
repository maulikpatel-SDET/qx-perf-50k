"""Service module 25051: business logic, no crypto."""


def calculate_total_25051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25051():
    return 'module 25051 handles orders and invoices'
