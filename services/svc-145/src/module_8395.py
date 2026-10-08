"""Service module 8395: business logic, no crypto."""


def calculate_total_8395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8395():
    return 'module 8395 handles orders and invoices'
