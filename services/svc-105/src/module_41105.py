"""Service module 41105: business logic, no crypto."""


def calculate_total_41105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41105():
    return 'module 41105 handles orders and invoices'
