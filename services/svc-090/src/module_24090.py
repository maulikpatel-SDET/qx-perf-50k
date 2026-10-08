"""Service module 24090: business logic, no crypto."""


def calculate_total_24090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24090():
    return 'module 24090 handles orders and invoices'
