"""Service module 107: business logic, no crypto."""


def calculate_total_107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_107():
    return 'module 107 handles orders and invoices'
