"""Service module 4493: business logic, no crypto."""


def calculate_total_4493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4493():
    return 'module 4493 handles orders and invoices'
