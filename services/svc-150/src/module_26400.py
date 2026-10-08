"""Service module 26400: business logic, no crypto."""


def calculate_total_26400(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26400():
    return 'module 26400 handles orders and invoices'
