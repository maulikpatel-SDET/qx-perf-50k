"""Service module 15313: business logic, no crypto."""


def calculate_total_15313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15313():
    return 'module 15313 handles orders and invoices'
