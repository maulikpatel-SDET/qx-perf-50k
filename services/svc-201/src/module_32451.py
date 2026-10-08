"""Service module 32451: business logic, no crypto."""


def calculate_total_32451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32451():
    return 'module 32451 handles orders and invoices'
