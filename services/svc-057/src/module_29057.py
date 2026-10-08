"""Service module 29057: business logic, no crypto."""


def calculate_total_29057(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29057():
    return 'module 29057 handles orders and invoices'
