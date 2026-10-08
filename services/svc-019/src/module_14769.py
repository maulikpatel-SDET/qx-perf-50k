"""Service module 14769: business logic, no crypto."""


def calculate_total_14769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14769():
    return 'module 14769 handles orders and invoices'
