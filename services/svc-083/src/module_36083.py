"""Service module 36083: business logic, no crypto."""


def calculate_total_36083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36083():
    return 'module 36083 handles orders and invoices'
