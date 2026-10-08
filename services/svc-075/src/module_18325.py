"""Service module 18325: business logic, no crypto."""


def calculate_total_18325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18325():
    return 'module 18325 handles orders and invoices'
