"""Service module 36375: business logic, no crypto."""


def calculate_total_36375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36375():
    return 'module 36375 handles orders and invoices'
