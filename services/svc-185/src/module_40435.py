"""Service module 40435: business logic, no crypto."""


def calculate_total_40435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40435():
    return 'module 40435 handles orders and invoices'
