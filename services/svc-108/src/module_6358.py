"""Service module 6358: business logic, no crypto."""


def calculate_total_6358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6358():
    return 'module 6358 handles orders and invoices'
