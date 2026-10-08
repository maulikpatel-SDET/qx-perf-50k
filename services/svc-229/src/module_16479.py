"""Service module 16479: business logic, no crypto."""


def calculate_total_16479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16479():
    return 'module 16479 handles orders and invoices'
