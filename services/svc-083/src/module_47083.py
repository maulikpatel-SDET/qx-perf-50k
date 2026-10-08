"""Service module 47083: business logic, no crypto."""


def calculate_total_47083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47083():
    return 'module 47083 handles orders and invoices'
