"""Service module 16372: business logic, no crypto."""


def calculate_total_16372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16372():
    return 'module 16372 handles orders and invoices'
