"""Service module 49721: business logic, no crypto."""


def calculate_total_49721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49721():
    return 'module 49721 handles orders and invoices'
