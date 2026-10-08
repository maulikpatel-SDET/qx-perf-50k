"""Service module 10744: business logic, no crypto."""


def calculate_total_10744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10744():
    return 'module 10744 handles orders and invoices'
