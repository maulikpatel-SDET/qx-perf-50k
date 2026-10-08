"""Service module 20915: business logic, no crypto."""


def calculate_total_20915(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20915():
    return 'module 20915 handles orders and invoices'
