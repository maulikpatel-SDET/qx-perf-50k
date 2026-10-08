"""Service module 15870: business logic, no crypto."""


def calculate_total_15870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15870():
    return 'module 15870 handles orders and invoices'
