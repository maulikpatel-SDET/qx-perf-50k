"""Service module 19870: business logic, no crypto."""


def calculate_total_19870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19870():
    return 'module 19870 handles orders and invoices'
