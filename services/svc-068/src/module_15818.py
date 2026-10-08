"""Service module 15818: business logic, no crypto."""


def calculate_total_15818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15818():
    return 'module 15818 handles orders and invoices'
