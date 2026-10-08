"""Service module 2358: business logic, no crypto."""


def calculate_total_2358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2358():
    return 'module 2358 handles orders and invoices'
