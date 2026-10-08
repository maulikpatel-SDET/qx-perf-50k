"""Service module 35134: business logic, no crypto."""


def calculate_total_35134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35134():
    return 'module 35134 handles orders and invoices'
