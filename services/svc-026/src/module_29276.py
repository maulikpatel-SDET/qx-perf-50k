"""Service module 29276: business logic, no crypto."""


def calculate_total_29276(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29276():
    return 'module 29276 handles orders and invoices'
