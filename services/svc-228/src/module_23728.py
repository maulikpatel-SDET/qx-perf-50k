"""Service module 23728: business logic, no crypto."""


def calculate_total_23728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23728():
    return 'module 23728 handles orders and invoices'
