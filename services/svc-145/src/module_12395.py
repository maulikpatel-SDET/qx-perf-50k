"""Service module 12395: business logic, no crypto."""


def calculate_total_12395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12395():
    return 'module 12395 handles orders and invoices'
