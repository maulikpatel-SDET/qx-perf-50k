"""Service module 47511: business logic, no crypto."""


def calculate_total_47511(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47511():
    return 'module 47511 handles orders and invoices'
