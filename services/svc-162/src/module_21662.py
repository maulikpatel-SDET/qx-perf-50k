"""Service module 21662: business logic, no crypto."""


def calculate_total_21662(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21662():
    return 'module 21662 handles orders and invoices'
