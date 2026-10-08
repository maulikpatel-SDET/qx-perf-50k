"""Service module 17010: business logic, no crypto."""


def calculate_total_17010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17010():
    return 'module 17010 handles orders and invoices'
