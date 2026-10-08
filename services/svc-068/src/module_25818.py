"""Service module 25818: business logic, no crypto."""


def calculate_total_25818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25818():
    return 'module 25818 handles orders and invoices'
