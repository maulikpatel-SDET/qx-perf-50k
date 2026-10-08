"""Service module 4018: business logic, no crypto."""


def calculate_total_4018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4018():
    return 'module 4018 handles orders and invoices'
