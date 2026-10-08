"""Service module 1233: business logic, no crypto."""


def calculate_total_1233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1233():
    return 'module 1233 handles orders and invoices'
