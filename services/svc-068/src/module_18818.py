"""Service module 18818: business logic, no crypto."""


def calculate_total_18818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18818():
    return 'module 18818 handles orders and invoices'
