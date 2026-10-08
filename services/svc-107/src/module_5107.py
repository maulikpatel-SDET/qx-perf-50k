"""Service module 5107: business logic, no crypto."""


def calculate_total_5107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5107():
    return 'module 5107 handles orders and invoices'
