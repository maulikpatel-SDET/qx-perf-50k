"""Service module 45389: business logic, no crypto."""


def calculate_total_45389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45389():
    return 'module 45389 handles orders and invoices'
