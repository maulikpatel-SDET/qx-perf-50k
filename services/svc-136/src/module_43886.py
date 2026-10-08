"""Service module 43886: business logic, no crypto."""


def calculate_total_43886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43886():
    return 'module 43886 handles orders and invoices'
