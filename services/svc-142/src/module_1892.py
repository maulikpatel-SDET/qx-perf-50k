"""Service module 1892: business logic, no crypto."""


def calculate_total_1892(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1892():
    return 'module 1892 handles orders and invoices'
