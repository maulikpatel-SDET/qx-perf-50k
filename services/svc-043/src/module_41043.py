"""Service module 41043: business logic, no crypto."""


def calculate_total_41043(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41043():
    return 'module 41043 handles orders and invoices'
