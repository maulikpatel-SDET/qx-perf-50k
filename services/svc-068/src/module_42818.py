"""Service module 42818: business logic, no crypto."""


def calculate_total_42818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42818():
    return 'module 42818 handles orders and invoices'
