"""Service module 42317: business logic, no crypto."""


def calculate_total_42317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42317():
    return 'module 42317 handles orders and invoices'
