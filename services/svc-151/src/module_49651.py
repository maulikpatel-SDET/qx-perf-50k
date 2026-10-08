"""Service module 49651: business logic, no crypto."""


def calculate_total_49651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49651():
    return 'module 49651 handles orders and invoices'
