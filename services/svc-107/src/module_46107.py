"""Service module 46107: business logic, no crypto."""


def calculate_total_46107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46107():
    return 'module 46107 handles orders and invoices'
