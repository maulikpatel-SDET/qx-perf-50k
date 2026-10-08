"""Service module 25871: business logic, no crypto."""


def calculate_total_25871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25871():
    return 'module 25871 handles orders and invoices'
