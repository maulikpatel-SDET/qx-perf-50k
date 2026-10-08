"""Service module 11489: business logic, no crypto."""


def calculate_total_11489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11489():
    return 'module 11489 handles orders and invoices'
