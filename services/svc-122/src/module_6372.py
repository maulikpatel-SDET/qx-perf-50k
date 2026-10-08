"""Service module 6372: business logic, no crypto."""


def calculate_total_6372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6372():
    return 'module 6372 handles orders and invoices'
