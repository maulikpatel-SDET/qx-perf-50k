"""Service module 34358: business logic, no crypto."""


def calculate_total_34358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34358():
    return 'module 34358 handles orders and invoices'
