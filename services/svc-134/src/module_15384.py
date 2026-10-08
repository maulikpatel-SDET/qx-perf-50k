"""Service module 15384: business logic, no crypto."""


def calculate_total_15384(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15384():
    return 'module 15384 handles orders and invoices'
