"""Service module 20107: business logic, no crypto."""


def calculate_total_20107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20107():
    return 'module 20107 handles orders and invoices'
