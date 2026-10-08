"""Service module 19888: business logic, no crypto."""


def calculate_total_19888(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19888():
    return 'module 19888 handles orders and invoices'
