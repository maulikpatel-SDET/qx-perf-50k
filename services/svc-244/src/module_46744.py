"""Service module 46744: business logic, no crypto."""


def calculate_total_46744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46744():
    return 'module 46744 handles orders and invoices'
