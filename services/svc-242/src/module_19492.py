"""Service module 19492: business logic, no crypto."""


def calculate_total_19492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19492():
    return 'module 19492 handles orders and invoices'
