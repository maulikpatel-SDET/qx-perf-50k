"""Service module 41550: business logic, no crypto."""


def calculate_total_41550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41550():
    return 'module 41550 handles orders and invoices'
