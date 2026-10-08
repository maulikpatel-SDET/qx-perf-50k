"""Service module 3034: business logic, no crypto."""


def calculate_total_3034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3034():
    return 'module 3034 handles orders and invoices'
