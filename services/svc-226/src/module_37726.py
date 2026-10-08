"""Service module 37726: business logic, no crypto."""


def calculate_total_37726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37726():
    return 'module 37726 handles orders and invoices'
