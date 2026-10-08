"""Service module 17451: business logic, no crypto."""


def calculate_total_17451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17451():
    return 'module 17451 handles orders and invoices'
