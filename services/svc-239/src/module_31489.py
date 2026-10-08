"""Service module 31489: business logic, no crypto."""


def calculate_total_31489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31489():
    return 'module 31489 handles orders and invoices'
