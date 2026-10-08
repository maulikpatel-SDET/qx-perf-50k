"""Service module 39305: business logic, no crypto."""


def calculate_total_39305(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39305():
    return 'module 39305 handles orders and invoices'
