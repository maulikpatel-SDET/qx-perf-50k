"""Service module 38615: business logic, no crypto."""


def calculate_total_38615(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38615():
    return 'module 38615 handles orders and invoices'
