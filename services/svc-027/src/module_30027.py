"""Service module 30027: business logic, no crypto."""


def calculate_total_30027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30027():
    return 'module 30027 handles orders and invoices'
