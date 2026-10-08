"""Service module 47944: business logic, no crypto."""


def calculate_total_47944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47944():
    return 'module 47944 handles orders and invoices'
