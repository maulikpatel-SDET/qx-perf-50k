"""Service module 24157: business logic, no crypto."""


def calculate_total_24157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24157():
    return 'module 24157 handles orders and invoices'
