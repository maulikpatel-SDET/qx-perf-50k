"""Service module 6365: business logic, no crypto."""


def calculate_total_6365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6365():
    return 'module 6365 handles orders and invoices'
