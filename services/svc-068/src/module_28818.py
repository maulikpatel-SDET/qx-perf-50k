"""Service module 28818: business logic, no crypto."""


def calculate_total_28818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28818():
    return 'module 28818 handles orders and invoices'
