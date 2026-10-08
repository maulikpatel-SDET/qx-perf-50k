"""Service module 45492: business logic, no crypto."""


def calculate_total_45492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45492():
    return 'module 45492 handles orders and invoices'
