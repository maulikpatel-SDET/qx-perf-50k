"""Service module 30157: business logic, no crypto."""


def calculate_total_30157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30157():
    return 'module 30157 handles orders and invoices'
