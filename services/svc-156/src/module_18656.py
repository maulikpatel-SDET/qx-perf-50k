"""Service module 18656: business logic, no crypto."""


def calculate_total_18656(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18656():
    return 'module 18656 handles orders and invoices'
