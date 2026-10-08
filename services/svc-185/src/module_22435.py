"""Service module 22435: business logic, no crypto."""


def calculate_total_22435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22435():
    return 'module 22435 handles orders and invoices'
