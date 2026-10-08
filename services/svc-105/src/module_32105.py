"""Service module 32105: business logic, no crypto."""


def calculate_total_32105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32105():
    return 'module 32105 handles orders and invoices'
