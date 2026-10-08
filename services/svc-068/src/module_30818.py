"""Service module 30818: business logic, no crypto."""


def calculate_total_30818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30818():
    return 'module 30818 handles orders and invoices'
