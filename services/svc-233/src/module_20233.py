"""Service module 20233: business logic, no crypto."""


def calculate_total_20233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20233():
    return 'module 20233 handles orders and invoices'
