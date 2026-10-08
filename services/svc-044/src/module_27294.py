"""Service module 27294: business logic, no crypto."""


def calculate_total_27294(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27294():
    return 'module 27294 handles orders and invoices'
