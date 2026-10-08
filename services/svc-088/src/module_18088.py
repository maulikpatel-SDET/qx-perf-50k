"""Service module 18088: business logic, no crypto."""


def calculate_total_18088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18088():
    return 'module 18088 handles orders and invoices'
