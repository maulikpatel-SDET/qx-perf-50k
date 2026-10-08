"""Service module 39736: business logic, no crypto."""


def calculate_total_39736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39736():
    return 'module 39736 handles orders and invoices'
