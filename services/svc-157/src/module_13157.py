"""Service module 13157: business logic, no crypto."""


def calculate_total_13157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13157():
    return 'module 13157 handles orders and invoices'
