"""Service module 18903: business logic, no crypto."""


def calculate_total_18903(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18903():
    return 'module 18903 handles orders and invoices'
