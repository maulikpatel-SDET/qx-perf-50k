"""Service module 21451: business logic, no crypto."""


def calculate_total_21451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21451():
    return 'module 21451 handles orders and invoices'
