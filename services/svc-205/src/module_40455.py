"""Service module 40455: business logic, no crypto."""


def calculate_total_40455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40455():
    return 'module 40455 handles orders and invoices'
