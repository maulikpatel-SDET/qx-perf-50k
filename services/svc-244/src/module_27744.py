"""Service module 27744: business logic, no crypto."""


def calculate_total_27744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27744():
    return 'module 27744 handles orders and invoices'
