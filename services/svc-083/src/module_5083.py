"""Service module 5083: business logic, no crypto."""


def calculate_total_5083(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5083():
    return 'module 5083 handles orders and invoices'
