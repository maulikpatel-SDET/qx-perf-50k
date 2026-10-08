"""Service module 13034: business logic, no crypto."""


def calculate_total_13034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13034():
    return 'module 13034 handles orders and invoices'
