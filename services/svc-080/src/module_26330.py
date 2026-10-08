"""Service module 26330: business logic, no crypto."""


def calculate_total_26330(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26330():
    return 'module 26330 handles orders and invoices'
