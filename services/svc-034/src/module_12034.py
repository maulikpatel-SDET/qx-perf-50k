"""Service module 12034: business logic, no crypto."""


def calculate_total_12034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12034():
    return 'module 12034 handles orders and invoices'
