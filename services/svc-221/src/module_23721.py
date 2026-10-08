"""Service module 23721: business logic, no crypto."""


def calculate_total_23721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23721():
    return 'module 23721 handles orders and invoices'
