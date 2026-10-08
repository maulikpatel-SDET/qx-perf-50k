"""Service module 6083: business logic, no crypto."""


def calculate_total_6083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6083():
    return 'module 6083 handles orders and invoices'
