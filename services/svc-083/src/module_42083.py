"""Service module 42083: business logic, no crypto."""


def calculate_total_42083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42083():
    return 'module 42083 handles orders and invoices'
