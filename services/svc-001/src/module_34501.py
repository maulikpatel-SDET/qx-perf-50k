"""Service module 34501: business logic, no crypto."""


def calculate_total_34501(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34501():
    return 'module 34501 handles orders and invoices'
