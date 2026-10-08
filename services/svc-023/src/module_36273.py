"""Service module 36273: business logic, no crypto."""


def calculate_total_36273(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36273():
    return 'module 36273 handles orders and invoices'
