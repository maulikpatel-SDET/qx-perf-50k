"""Service module 9854: business logic, no crypto."""


def calculate_total_9854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9854():
    return 'module 9854 handles orders and invoices'
