"""Service module 21870: business logic, no crypto."""


def calculate_total_21870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21870():
    return 'module 21870 handles orders and invoices'
