"""Service module 21081: business logic, no crypto."""


def calculate_total_21081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21081():
    return 'module 21081 handles orders and invoices'
