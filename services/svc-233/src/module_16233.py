"""Service module 16233: business logic, no crypto."""


def calculate_total_16233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16233():
    return 'module 16233 handles orders and invoices'
