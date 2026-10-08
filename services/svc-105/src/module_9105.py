"""Service module 9105: business logic, no crypto."""


def calculate_total_9105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9105():
    return 'module 9105 handles orders and invoices'
