"""Service module 29854: business logic, no crypto."""


def calculate_total_29854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29854():
    return 'module 29854 handles orders and invoices'
