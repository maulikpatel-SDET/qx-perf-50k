"""Service module 37033: business logic, no crypto."""


def calculate_total_37033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37033():
    return 'module 37033 handles orders and invoices'
