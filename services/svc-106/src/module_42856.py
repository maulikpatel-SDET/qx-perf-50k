"""Service module 42856: business logic, no crypto."""


def calculate_total_42856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42856():
    return 'module 42856 handles orders and invoices'
