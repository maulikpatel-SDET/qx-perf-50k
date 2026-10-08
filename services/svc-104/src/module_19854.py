"""Service module 19854: business logic, no crypto."""


def calculate_total_19854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19854():
    return 'module 19854 handles orders and invoices'
