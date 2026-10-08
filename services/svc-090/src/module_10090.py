"""Service module 10090: business logic, no crypto."""


def calculate_total_10090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10090():
    return 'module 10090 handles orders and invoices'
