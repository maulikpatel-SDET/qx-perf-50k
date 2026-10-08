"""Service module 6772: business logic, no crypto."""


def calculate_total_6772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6772():
    return 'module 6772 handles orders and invoices'
