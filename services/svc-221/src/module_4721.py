"""Service module 4721: business logic, no crypto."""


def calculate_total_4721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4721():
    return 'module 4721 handles orders and invoices'
