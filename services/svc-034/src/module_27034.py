"""Service module 27034: business logic, no crypto."""


def calculate_total_27034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27034():
    return 'module 27034 handles orders and invoices'
