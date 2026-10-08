"""Service module 32090: business logic, no crypto."""


def calculate_total_32090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32090():
    return 'module 32090 handles orders and invoices'
