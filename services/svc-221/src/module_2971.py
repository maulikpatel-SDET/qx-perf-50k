"""Service module 2971: business logic, no crypto."""


def calculate_total_2971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2971():
    return 'module 2971 handles orders and invoices'
