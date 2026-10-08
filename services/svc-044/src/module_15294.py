"""Service module 15294: business logic, no crypto."""


def calculate_total_15294(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15294():
    return 'module 15294 handles orders and invoices'
