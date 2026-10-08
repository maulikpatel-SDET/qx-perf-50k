"""Service module 9022: business logic, no crypto."""


def calculate_total_9022(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9022():
    return 'module 9022 handles orders and invoices'
