"""Service module 37769: business logic, no crypto."""


def calculate_total_37769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37769():
    return 'module 37769 handles orders and invoices'
