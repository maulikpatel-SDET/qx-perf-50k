"""Service module 12090: business logic, no crypto."""


def calculate_total_12090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12090():
    return 'module 12090 handles orders and invoices'
