"""Service module 20818: business logic, no crypto."""


def calculate_total_20818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20818():
    return 'module 20818 handles orders and invoices'
