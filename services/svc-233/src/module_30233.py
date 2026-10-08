"""Service module 30233: business logic, no crypto."""


def calculate_total_30233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30233():
    return 'module 30233 handles orders and invoices'
