"""Service module 18132: business logic, no crypto."""


def calculate_total_18132(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18132():
    return 'module 18132 handles orders and invoices'
