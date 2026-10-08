"""Service module 41462: business logic, no crypto."""


def calculate_total_41462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41462():
    return 'module 41462 handles orders and invoices'
