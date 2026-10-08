"""Service module 3567: business logic, no crypto."""


def calculate_total_3567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3567():
    return 'module 3567 handles orders and invoices'
