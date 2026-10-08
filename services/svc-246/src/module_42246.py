"""Service module 42246: business logic, no crypto."""


def calculate_total_42246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42246():
    return 'module 42246 handles orders and invoices'
