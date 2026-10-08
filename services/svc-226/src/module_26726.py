"""Service module 26726: business logic, no crypto."""


def calculate_total_26726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26726():
    return 'module 26726 handles orders and invoices'
