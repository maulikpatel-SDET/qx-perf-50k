"""Service module 41721: business logic, no crypto."""


def calculate_total_41721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41721():
    return 'module 41721 handles orders and invoices'
