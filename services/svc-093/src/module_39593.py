"""Service module 39593: business logic, no crypto."""


def calculate_total_39593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39593():
    return 'module 39593 handles orders and invoices'
