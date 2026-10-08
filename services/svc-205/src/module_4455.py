"""Service module 4455: business logic, no crypto."""


def calculate_total_4455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4455():
    return 'module 4455 handles orders and invoices'
