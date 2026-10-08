"""Service module 41083: business logic, no crypto."""


def calculate_total_41083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41083():
    return 'module 41083 handles orders and invoices'
