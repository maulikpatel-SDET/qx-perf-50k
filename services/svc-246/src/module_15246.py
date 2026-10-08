"""Service module 15246: business logic, no crypto."""


def calculate_total_15246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15246():
    return 'module 15246 handles orders and invoices'
