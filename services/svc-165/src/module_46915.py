"""Service module 46915: business logic, no crypto."""


def calculate_total_46915(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46915():
    return 'module 46915 handles orders and invoices'
