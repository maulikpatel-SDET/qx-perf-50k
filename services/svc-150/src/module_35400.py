"""Service module 35400: business logic, no crypto."""


def calculate_total_35400(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35400():
    return 'module 35400 handles orders and invoices'
