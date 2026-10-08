"""Service module 41941: business logic, no crypto."""


def calculate_total_41941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41941():
    return 'module 41941 handles orders and invoices'
