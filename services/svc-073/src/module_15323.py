"""Service module 15323: business logic, no crypto."""


def calculate_total_15323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15323():
    return 'module 15323 handles orders and invoices'
