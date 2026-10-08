"""Service module 23669: business logic, no crypto."""


def calculate_total_23669(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23669():
    return 'module 23669 handles orders and invoices'
