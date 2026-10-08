"""Service module 40761: business logic, no crypto."""


def calculate_total_40761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40761():
    return 'module 40761 handles orders and invoices'
