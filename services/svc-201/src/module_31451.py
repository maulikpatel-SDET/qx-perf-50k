"""Service module 31451: business logic, no crypto."""


def calculate_total_31451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31451():
    return 'module 31451 handles orders and invoices'
