"""Service module 45395: business logic, no crypto."""


def calculate_total_45395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45395():
    return 'module 45395 handles orders and invoices'
