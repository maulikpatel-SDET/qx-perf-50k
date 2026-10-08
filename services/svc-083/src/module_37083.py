"""Service module 37083: business logic, no crypto."""


def calculate_total_37083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37083():
    return 'module 37083 handles orders and invoices'
