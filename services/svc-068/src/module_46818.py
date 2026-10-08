"""Service module 46818: business logic, no crypto."""


def calculate_total_46818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46818():
    return 'module 46818 handles orders and invoices'
