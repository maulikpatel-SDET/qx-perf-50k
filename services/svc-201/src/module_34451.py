"""Service module 34451: business logic, no crypto."""


def calculate_total_34451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34451():
    return 'module 34451 handles orders and invoices'
