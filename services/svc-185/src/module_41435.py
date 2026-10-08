"""Service module 41435: business logic, no crypto."""


def calculate_total_41435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41435():
    return 'module 41435 handles orders and invoices'
