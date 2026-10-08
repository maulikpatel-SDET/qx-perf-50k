"""Service module 24313: business logic, no crypto."""


def calculate_total_24313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24313():
    return 'module 24313 handles orders and invoices'
