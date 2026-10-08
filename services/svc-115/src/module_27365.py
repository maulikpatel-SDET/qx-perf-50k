"""Service module 27365: business logic, no crypto."""


def calculate_total_27365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27365():
    return 'module 27365 handles orders and invoices'
