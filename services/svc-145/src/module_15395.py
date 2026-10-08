"""Service module 15395: business logic, no crypto."""


def calculate_total_15395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15395():
    return 'module 15395 handles orders and invoices'
