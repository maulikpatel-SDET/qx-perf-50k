"""Service module 38451: business logic, no crypto."""


def calculate_total_38451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38451():
    return 'module 38451 handles orders and invoices'
