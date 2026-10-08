"""Service module 13083: business logic, no crypto."""


def calculate_total_13083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13083():
    return 'module 13083 handles orders and invoices'
