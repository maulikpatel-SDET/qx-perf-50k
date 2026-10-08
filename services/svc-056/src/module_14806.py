"""Service module 14806: business logic, no crypto."""


def calculate_total_14806(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14806():
    return 'module 14806 handles orders and invoices'
