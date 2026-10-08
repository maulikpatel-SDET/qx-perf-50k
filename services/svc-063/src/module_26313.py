"""Service module 26313: business logic, no crypto."""


def calculate_total_26313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26313():
    return 'module 26313 handles orders and invoices'
