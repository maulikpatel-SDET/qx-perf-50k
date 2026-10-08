"""Service module 27388: business logic, no crypto."""


def calculate_total_27388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27388():
    return 'module 27388 handles orders and invoices'
