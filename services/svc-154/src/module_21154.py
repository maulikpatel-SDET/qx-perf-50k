"""Service module 21154: business logic, no crypto."""


def calculate_total_21154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21154():
    return 'module 21154 handles orders and invoices'
