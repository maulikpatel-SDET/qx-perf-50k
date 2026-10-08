"""Service module 32107: business logic, no crypto."""


def calculate_total_32107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32107():
    return 'module 32107 handles orders and invoices'
