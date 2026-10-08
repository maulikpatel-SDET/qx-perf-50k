"""Service module 2138: business logic, no crypto."""


def calculate_total_2138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2138():
    return 'module 2138 handles orders and invoices'
