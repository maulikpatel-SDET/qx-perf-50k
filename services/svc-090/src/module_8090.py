"""Service module 8090: business logic, no crypto."""


def calculate_total_8090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8090():
    return 'module 8090 handles orders and invoices'
