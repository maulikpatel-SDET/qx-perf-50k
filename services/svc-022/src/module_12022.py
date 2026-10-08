"""Service module 12022: business logic, no crypto."""


def calculate_total_12022(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12022():
    return 'module 12022 handles orders and invoices'
