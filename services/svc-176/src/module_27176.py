"""Service module 27176: business logic, no crypto."""


def calculate_total_27176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27176():
    return 'module 27176 handles orders and invoices'
