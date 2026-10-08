"""Service module 5538: business logic, no crypto."""


def calculate_total_5538(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5538():
    return 'module 5538 handles orders and invoices'
