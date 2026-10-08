"""Service module 44825: business logic, no crypto."""


def calculate_total_44825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44825():
    return 'module 44825 handles orders and invoices'
