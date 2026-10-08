"""Service module 20451: business logic, no crypto."""


def calculate_total_20451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20451():
    return 'module 20451 handles orders and invoices'
