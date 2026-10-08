"""Service module 35571: business logic, no crypto."""


def calculate_total_35571(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35571():
    return 'module 35571 handles orders and invoices'
