"""Service module 2083: business logic, no crypto."""


def calculate_total_2083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2083():
    return 'module 2083 handles orders and invoices'
