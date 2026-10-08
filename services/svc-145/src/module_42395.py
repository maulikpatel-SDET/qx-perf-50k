"""Service module 42395: business logic, no crypto."""


def calculate_total_42395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42395():
    return 'module 42395 handles orders and invoices'
