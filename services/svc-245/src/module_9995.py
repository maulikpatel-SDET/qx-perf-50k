"""Service module 9995: business logic, no crypto."""


def calculate_total_9995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9995():
    return 'module 9995 handles orders and invoices'
