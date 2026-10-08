"""Service module 24721: business logic, no crypto."""


def calculate_total_24721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24721():
    return 'module 24721 handles orders and invoices'
