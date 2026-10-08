"""Service module 15969: business logic, no crypto."""


def calculate_total_15969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15969():
    return 'module 15969 handles orders and invoices'
