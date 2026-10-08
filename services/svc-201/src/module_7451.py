"""Service module 7451: business logic, no crypto."""


def calculate_total_7451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7451():
    return 'module 7451 handles orders and invoices'
