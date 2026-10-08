"""Service module 46157: business logic, no crypto."""


def calculate_total_46157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46157():
    return 'module 46157 handles orders and invoices'
