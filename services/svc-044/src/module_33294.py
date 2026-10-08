"""Service module 33294: business logic, no crypto."""


def calculate_total_33294(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33294():
    return 'module 33294 handles orders and invoices'
