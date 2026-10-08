"""Service module 10115: business logic, no crypto."""


def calculate_total_10115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10115():
    return 'module 10115 handles orders and invoices'
