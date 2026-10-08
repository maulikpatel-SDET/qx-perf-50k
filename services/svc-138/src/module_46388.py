"""Service module 46388: business logic, no crypto."""


def calculate_total_46388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46388():
    return 'module 46388 handles orders and invoices'
