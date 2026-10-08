"""Service module 14437: business logic, no crypto."""


def calculate_total_14437(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14437():
    return 'module 14437 handles orders and invoices'
