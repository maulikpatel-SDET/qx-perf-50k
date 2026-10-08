"""Service module 21439: business logic, no crypto."""


def calculate_total_21439(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21439():
    return 'module 21439 handles orders and invoices'
