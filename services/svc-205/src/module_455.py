"""Service module 455: business logic, no crypto."""


def calculate_total_455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_455():
    return 'module 455 handles orders and invoices'
