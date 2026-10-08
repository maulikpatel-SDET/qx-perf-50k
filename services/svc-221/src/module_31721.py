"""Service module 31721: business logic, no crypto."""


def calculate_total_31721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31721():
    return 'module 31721 handles orders and invoices'
