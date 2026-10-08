"""Service module 42276: business logic, no crypto."""


def calculate_total_42276(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42276():
    return 'module 42276 handles orders and invoices'
