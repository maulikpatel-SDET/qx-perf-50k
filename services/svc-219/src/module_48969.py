"""Service module 48969: business logic, no crypto."""


def calculate_total_48969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48969():
    return 'module 48969 handles orders and invoices'
