"""Service module 25158: business logic, no crypto."""


def calculate_total_25158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25158():
    return 'module 25158 handles orders and invoices'
