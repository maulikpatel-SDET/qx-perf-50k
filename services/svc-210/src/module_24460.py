"""Service module 24460: business logic, no crypto."""


def calculate_total_24460(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24460():
    return 'module 24460 handles orders and invoices'
