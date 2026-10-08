"""Service module 36304: business logic, no crypto."""


def calculate_total_36304(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36304():
    return 'module 36304 handles orders and invoices'
