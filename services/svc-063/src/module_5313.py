"""Service module 5313: business logic, no crypto."""


def calculate_total_5313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5313():
    return 'module 5313 handles orders and invoices'
