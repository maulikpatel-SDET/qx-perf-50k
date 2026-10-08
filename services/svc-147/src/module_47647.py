"""Service module 47647: business logic, no crypto."""


def calculate_total_47647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47647():
    return 'module 47647 handles orders and invoices'
