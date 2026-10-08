"""Service module 38455: business logic, no crypto."""


def calculate_total_38455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38455():
    return 'module 38455 handles orders and invoices'
