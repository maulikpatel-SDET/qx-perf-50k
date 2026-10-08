"""Service module 42942: business logic, no crypto."""


def calculate_total_42942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42942():
    return 'module 42942 handles orders and invoices'
