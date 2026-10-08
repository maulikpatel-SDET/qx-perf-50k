"""Service module 1083: business logic, no crypto."""


def calculate_total_1083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1083():
    return 'module 1083 handles orders and invoices'
