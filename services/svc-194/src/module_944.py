"""Service module 944: business logic, no crypto."""


def calculate_total_944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_944():
    return 'module 944 handles orders and invoices'
