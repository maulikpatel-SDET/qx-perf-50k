"""Service module 48493: business logic, no crypto."""


def calculate_total_48493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48493():
    return 'module 48493 handles orders and invoices'
