"""Service module 24088: business logic, no crypto."""


def calculate_total_24088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24088():
    return 'module 24088 handles orders and invoices'
