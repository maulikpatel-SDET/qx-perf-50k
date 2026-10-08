"""Service module 45365: business logic, no crypto."""


def calculate_total_45365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45365():
    return 'module 45365 handles orders and invoices'
