"""Service module 24821: business logic, no crypto."""


def calculate_total_24821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24821():
    return 'module 24821 handles orders and invoices'
