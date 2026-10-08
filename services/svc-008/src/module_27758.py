"""Service module 27758: business logic, no crypto."""


def calculate_total_27758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27758():
    return 'module 27758 handles orders and invoices'
