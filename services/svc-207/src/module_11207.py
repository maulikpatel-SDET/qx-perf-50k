"""Service module 11207: business logic, no crypto."""


def calculate_total_11207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11207():
    return 'module 11207 handles orders and invoices'
