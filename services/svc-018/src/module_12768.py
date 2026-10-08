"""Service module 12768: business logic, no crypto."""


def calculate_total_12768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12768():
    return 'module 12768 handles orders and invoices'
