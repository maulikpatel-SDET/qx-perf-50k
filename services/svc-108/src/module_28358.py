"""Service module 28358: business logic, no crypto."""


def calculate_total_28358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28358():
    return 'module 28358 handles orders and invoices'
