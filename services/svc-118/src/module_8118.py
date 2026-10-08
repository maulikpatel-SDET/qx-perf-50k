"""Service module 8118: business logic, no crypto."""


def calculate_total_8118(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8118():
    return 'module 8118 handles orders and invoices'
