"""Service module 818: business logic, no crypto."""


def calculate_total_818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_818():
    return 'module 818 handles orders and invoices'
