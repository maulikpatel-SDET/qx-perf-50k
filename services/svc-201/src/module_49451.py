"""Service module 49451: business logic, no crypto."""


def calculate_total_49451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49451():
    return 'module 49451 handles orders and invoices'
