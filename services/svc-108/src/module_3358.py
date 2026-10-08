"""Service module 3358: business logic, no crypto."""


def calculate_total_3358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3358():
    return 'module 3358 handles orders and invoices'
