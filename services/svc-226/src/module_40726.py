"""Service module 40726: business logic, no crypto."""


def calculate_total_40726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40726():
    return 'module 40726 handles orders and invoices'
