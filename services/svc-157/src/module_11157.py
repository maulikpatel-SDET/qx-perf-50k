"""Service module 11157: business logic, no crypto."""


def calculate_total_11157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11157():
    return 'module 11157 handles orders and invoices'
