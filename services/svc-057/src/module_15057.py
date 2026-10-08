"""Service module 15057: business logic, no crypto."""


def calculate_total_15057(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15057():
    return 'module 15057 handles orders and invoices'
