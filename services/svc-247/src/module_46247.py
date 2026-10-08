"""Service module 46247: business logic, no crypto."""


def calculate_total_46247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46247():
    return 'module 46247 handles orders and invoices'
