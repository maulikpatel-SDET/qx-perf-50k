"""Service module 40107: business logic, no crypto."""


def calculate_total_40107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40107():
    return 'module 40107 handles orders and invoices'
