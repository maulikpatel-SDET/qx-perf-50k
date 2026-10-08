"""Service module 41107: business logic, no crypto."""


def calculate_total_41107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41107():
    return 'module 41107 handles orders and invoices'
