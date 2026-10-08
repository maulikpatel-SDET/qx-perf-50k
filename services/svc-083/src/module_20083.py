"""Service module 20083: business logic, no crypto."""


def calculate_total_20083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20083():
    return 'module 20083 handles orders and invoices'
