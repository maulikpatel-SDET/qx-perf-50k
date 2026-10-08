"""Service module 13726: business logic, no crypto."""


def calculate_total_13726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13726():
    return 'module 13726 handles orders and invoices'
