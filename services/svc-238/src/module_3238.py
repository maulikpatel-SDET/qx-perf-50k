"""Service module 3238: business logic, no crypto."""


def calculate_total_3238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3238():
    return 'module 3238 handles orders and invoices'
