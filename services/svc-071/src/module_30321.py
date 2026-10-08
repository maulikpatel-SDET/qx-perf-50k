"""Service module 30321: business logic, no crypto."""


def calculate_total_30321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30321():
    return 'module 30321 handles orders and invoices'
