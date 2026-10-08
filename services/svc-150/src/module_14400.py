"""Service module 14400: business logic, no crypto."""


def calculate_total_14400(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14400():
    return 'module 14400 handles orders and invoices'
