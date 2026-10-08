"""Service module 6276: business logic, no crypto."""


def calculate_total_6276(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6276():
    return 'module 6276 handles orders and invoices'
