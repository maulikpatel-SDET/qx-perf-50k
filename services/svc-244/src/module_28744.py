"""Service module 28744: business logic, no crypto."""


def calculate_total_28744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28744():
    return 'module 28744 handles orders and invoices'
