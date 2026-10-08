"""Service module 5537: business logic, no crypto."""


def calculate_total_5537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5537():
    return 'module 5537 handles orders and invoices'
