"""Service module 8492: business logic, no crypto."""


def calculate_total_8492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8492():
    return 'module 8492 handles orders and invoices'
