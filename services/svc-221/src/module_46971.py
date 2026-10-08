"""Service module 46971: business logic, no crypto."""


def calculate_total_46971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46971():
    return 'module 46971 handles orders and invoices'
