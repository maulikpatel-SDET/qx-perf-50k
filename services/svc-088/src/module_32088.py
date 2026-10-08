"""Service module 32088: business logic, no crypto."""


def calculate_total_32088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32088():
    return 'module 32088 handles orders and invoices'
