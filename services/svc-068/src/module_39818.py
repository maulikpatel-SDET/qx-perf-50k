"""Service module 39818: business logic, no crypto."""


def calculate_total_39818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39818():
    return 'module 39818 handles orders and invoices'
