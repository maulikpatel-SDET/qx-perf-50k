"""Service module 14559: business logic, no crypto."""


def calculate_total_14559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14559():
    return 'module 14559 handles orders and invoices'
