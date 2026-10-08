"""Service module 33451: business logic, no crypto."""


def calculate_total_33451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33451():
    return 'module 33451 handles orders and invoices'
