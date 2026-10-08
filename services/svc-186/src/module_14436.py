"""Service module 14436: business logic, no crypto."""


def calculate_total_14436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14436():
    return 'module 14436 handles orders and invoices'
