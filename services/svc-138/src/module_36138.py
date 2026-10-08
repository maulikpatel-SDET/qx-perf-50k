"""Service module 36138: business logic, no crypto."""


def calculate_total_36138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36138():
    return 'module 36138 handles orders and invoices'
