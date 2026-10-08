"""Service module 26593: business logic, no crypto."""


def calculate_total_26593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26593():
    return 'module 26593 handles orders and invoices'
