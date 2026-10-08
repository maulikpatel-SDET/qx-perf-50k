"""Service module 12372: business logic, no crypto."""


def calculate_total_12372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12372():
    return 'module 12372 handles orders and invoices'
