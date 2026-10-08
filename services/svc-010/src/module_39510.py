"""Service module 39510: business logic, no crypto."""


def calculate_total_39510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39510():
    return 'module 39510 handles orders and invoices'
