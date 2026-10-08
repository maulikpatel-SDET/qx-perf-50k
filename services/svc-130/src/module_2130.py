"""Service module 2130: business logic, no crypto."""


def calculate_total_2130(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2130():
    return 'module 2130 handles orders and invoices'
