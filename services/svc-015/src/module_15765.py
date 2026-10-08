"""Service module 15765: business logic, no crypto."""


def calculate_total_15765(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15765():
    return 'module 15765 handles orders and invoices'
