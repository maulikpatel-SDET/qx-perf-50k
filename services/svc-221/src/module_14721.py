"""Service module 14721: business logic, no crypto."""


def calculate_total_14721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14721():
    return 'module 14721 handles orders and invoices'
