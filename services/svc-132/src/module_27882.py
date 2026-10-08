"""Service module 27882: business logic, no crypto."""


def calculate_total_27882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27882():
    return 'module 27882 handles orders and invoices'
