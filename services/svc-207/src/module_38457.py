"""Service module 38457: business logic, no crypto."""


def calculate_total_38457(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38457():
    return 'module 38457 handles orders and invoices'
