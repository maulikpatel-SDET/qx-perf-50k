"""Service module 32083: business logic, no crypto."""


def calculate_total_32083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32083():
    return 'module 32083 handles orders and invoices'
