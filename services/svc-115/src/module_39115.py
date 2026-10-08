"""Service module 39115: business logic, no crypto."""


def calculate_total_39115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39115():
    return 'module 39115 handles orders and invoices'
