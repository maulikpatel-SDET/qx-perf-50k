"""Service module 21854: business logic, no crypto."""


def calculate_total_21854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21854():
    return 'module 21854 handles orders and invoices'
