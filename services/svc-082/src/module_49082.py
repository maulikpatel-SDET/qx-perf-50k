"""Service module 49082: business logic, no crypto."""


def calculate_total_49082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49082():
    return 'module 49082 handles orders and invoices'
