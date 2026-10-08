"""Service module 42481: business logic, no crypto."""


def calculate_total_42481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42481():
    return 'module 42481 handles orders and invoices'
