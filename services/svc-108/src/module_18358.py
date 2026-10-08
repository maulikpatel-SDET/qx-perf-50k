"""Service module 18358: business logic, no crypto."""


def calculate_total_18358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18358():
    return 'module 18358 handles orders and invoices'
