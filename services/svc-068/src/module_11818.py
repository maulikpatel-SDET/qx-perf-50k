"""Service module 11818: business logic, no crypto."""


def calculate_total_11818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11818():
    return 'module 11818 handles orders and invoices'
