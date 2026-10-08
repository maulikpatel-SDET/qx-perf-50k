"""Service module 42107: business logic, no crypto."""


def calculate_total_42107(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42107():
    return 'module 42107 handles orders and invoices'
