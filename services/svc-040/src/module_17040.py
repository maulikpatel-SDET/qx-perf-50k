"""Service module 17040: business logic, no crypto."""


def calculate_total_17040(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17040():
    return 'module 17040 handles orders and invoices'
