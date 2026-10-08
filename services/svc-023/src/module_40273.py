"""Service module 40273: business logic, no crypto."""


def calculate_total_40273(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40273():
    return 'module 40273 handles orders and invoices'
