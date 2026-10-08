"""Service module 6395: business logic, no crypto."""


def calculate_total_6395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6395():
    return 'module 6395 handles orders and invoices'
