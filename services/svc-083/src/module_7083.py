"""Service module 7083: business logic, no crypto."""


def calculate_total_7083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7083():
    return 'module 7083 handles orders and invoices'
