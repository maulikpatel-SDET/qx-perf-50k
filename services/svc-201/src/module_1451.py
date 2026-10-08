"""Service module 1451: business logic, no crypto."""


def calculate_total_1451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1451():
    return 'module 1451 handles orders and invoices'
