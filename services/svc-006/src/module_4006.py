"""Service module 4006: business logic, no crypto."""


def calculate_total_4006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4006():
    return 'module 4006 handles orders and invoices'
