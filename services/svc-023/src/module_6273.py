"""Service module 6273: business logic, no crypto."""


def calculate_total_6273(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6273():
    return 'module 6273 handles orders and invoices'
