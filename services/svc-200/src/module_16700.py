"""Service module 16700: business logic, no crypto."""


def calculate_total_16700(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16700():
    return 'module 16700 handles orders and invoices'
