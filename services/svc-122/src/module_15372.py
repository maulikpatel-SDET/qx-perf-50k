"""Service module 15372: business logic, no crypto."""


def calculate_total_15372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15372():
    return 'module 15372 handles orders and invoices'
