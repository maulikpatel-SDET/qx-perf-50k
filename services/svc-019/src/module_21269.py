"""Service module 21269: business logic, no crypto."""


def calculate_total_21269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21269():
    return 'module 21269 handles orders and invoices'
