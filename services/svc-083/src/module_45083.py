"""Service module 45083: business logic, no crypto."""


def calculate_total_45083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45083():
    return 'module 45083 handles orders and invoices'
