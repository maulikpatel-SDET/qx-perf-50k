"""Service module 27004: business logic, no crypto."""


def calculate_total_27004(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27004():
    return 'module 27004 handles orders and invoices'
