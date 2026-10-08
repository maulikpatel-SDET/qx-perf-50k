"""Service module 26063: business logic, no crypto."""


def calculate_total_26063(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26063():
    return 'module 26063 handles orders and invoices'
