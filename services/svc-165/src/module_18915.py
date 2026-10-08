"""Service module 18915: business logic, no crypto."""


def calculate_total_18915(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18915():
    return 'module 18915 handles orders and invoices'
