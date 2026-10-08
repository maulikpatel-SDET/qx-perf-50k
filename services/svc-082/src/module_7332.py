"""Service module 7332: business logic, no crypto."""


def calculate_total_7332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7332():
    return 'module 7332 handles orders and invoices'
