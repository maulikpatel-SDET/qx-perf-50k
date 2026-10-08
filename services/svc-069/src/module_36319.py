"""Service module 36319: business logic, no crypto."""


def calculate_total_36319(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36319():
    return 'module 36319 handles orders and invoices'
