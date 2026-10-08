"""Service module 49455: business logic, no crypto."""


def calculate_total_49455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49455():
    return 'module 49455 handles orders and invoices'
