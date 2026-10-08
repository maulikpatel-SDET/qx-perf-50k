"""Service module 31435: business logic, no crypto."""


def calculate_total_31435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31435():
    return 'module 31435 handles orders and invoices'
