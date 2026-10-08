"""Service module 15599: business logic, no crypto."""


def calculate_total_15599(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15599():
    return 'module 15599 handles orders and invoices'
