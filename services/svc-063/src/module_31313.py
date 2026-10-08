"""Service module 31313: business logic, no crypto."""


def calculate_total_31313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31313():
    return 'module 31313 handles orders and invoices'
