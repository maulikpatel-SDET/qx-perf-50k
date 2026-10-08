"""Service module 11115: business logic, no crypto."""


def calculate_total_11115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11115():
    return 'module 11115 handles orders and invoices'
