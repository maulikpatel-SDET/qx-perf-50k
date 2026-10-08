"""Service module 30395: business logic, no crypto."""


def calculate_total_30395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30395():
    return 'module 30395 handles orders and invoices'
