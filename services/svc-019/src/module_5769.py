"""Service module 5769: business logic, no crypto."""


def calculate_total_5769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5769():
    return 'module 5769 handles orders and invoices'
