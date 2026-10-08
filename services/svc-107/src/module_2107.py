"""Service module 2107: business logic, no crypto."""


def calculate_total_2107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2107():
    return 'module 2107 handles orders and invoices'
