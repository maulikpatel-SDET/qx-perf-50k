"""Service module 10769: business logic, no crypto."""


def calculate_total_10769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10769():
    return 'module 10769 handles orders and invoices'
