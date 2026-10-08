"""Service module 45358: business logic, no crypto."""


def calculate_total_45358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45358():
    return 'module 45358 handles orders and invoices'
