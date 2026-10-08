"""Service module 31090: business logic, no crypto."""


def calculate_total_31090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31090():
    return 'module 31090 handles orders and invoices'
