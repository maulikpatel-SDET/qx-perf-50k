"""Service module 4489: business logic, no crypto."""


def calculate_total_4489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4489():
    return 'module 4489 handles orders and invoices'
