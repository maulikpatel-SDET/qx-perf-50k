"""Service module 28721: business logic, no crypto."""


def calculate_total_28721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28721():
    return 'module 28721 handles orders and invoices'
