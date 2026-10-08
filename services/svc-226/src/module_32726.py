"""Service module 32726: business logic, no crypto."""


def calculate_total_32726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32726():
    return 'module 32726 handles orders and invoices'
