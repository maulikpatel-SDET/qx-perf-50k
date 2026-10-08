"""Service module 37140: business logic, no crypto."""


def calculate_total_37140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37140():
    return 'module 37140 handles orders and invoices'
