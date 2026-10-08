"""Service module 13138: business logic, no crypto."""


def calculate_total_13138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13138():
    return 'module 13138 handles orders and invoices'
