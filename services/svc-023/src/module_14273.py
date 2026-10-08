"""Service module 14273: business logic, no crypto."""


def calculate_total_14273(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14273():
    return 'module 14273 handles orders and invoices'
