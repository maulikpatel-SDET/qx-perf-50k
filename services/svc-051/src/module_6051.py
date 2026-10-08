"""Service module 6051: business logic, no crypto."""


def calculate_total_6051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6051():
    return 'module 6051 handles orders and invoices'
