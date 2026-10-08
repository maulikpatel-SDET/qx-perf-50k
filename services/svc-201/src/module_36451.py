"""Service module 36451: business logic, no crypto."""


def calculate_total_36451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36451():
    return 'module 36451 handles orders and invoices'
