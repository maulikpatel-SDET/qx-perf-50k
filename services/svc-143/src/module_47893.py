"""Service module 47893: business logic, no crypto."""


def calculate_total_47893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47893():
    return 'module 47893 handles orders and invoices'
