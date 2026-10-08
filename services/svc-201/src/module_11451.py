"""Service module 11451: business logic, no crypto."""


def calculate_total_11451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11451():
    return 'module 11451 handles orders and invoices'
