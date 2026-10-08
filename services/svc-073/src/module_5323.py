"""Service module 5323: business logic, no crypto."""


def calculate_total_5323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5323():
    return 'module 5323 handles orders and invoices'
