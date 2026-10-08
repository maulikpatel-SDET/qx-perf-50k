"""Service module 44358: business logic, no crypto."""


def calculate_total_44358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44358():
    return 'module 44358 handles orders and invoices'
