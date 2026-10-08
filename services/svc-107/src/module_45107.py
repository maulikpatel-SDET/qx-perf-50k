"""Service module 45107: business logic, no crypto."""


def calculate_total_45107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45107():
    return 'module 45107 handles orders and invoices'
